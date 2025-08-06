import django_filters
from django.db import models
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from products.filters import ProductFilter

from products.models import  Product
from products.serializers import  ProductSerializers
from products.permissions import IsStaffOrReadOnly




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']


    permission_classes = [IsStaffOrReadOnly]

    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        is_new = request.query_params.get('is_new', None)
        if category:
            self.queryset = self.queryset.filter(category=category)
        if is_new is not None:
            self.queryset = self.queryset.filter(is_new=True)
            return super().list(request, *args, *kwargs)




    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_products = Product.objects.filter(category = instance.category).exclude(id=instance.id)[:5]
        related_serializer = ProductSerializers(related_products, many=True)
        return Response({
            "product": serializer.data,
            "related_products": related_serializer.data
        })


    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        top_products = Product.objects.annotate(avg_rating=models.Avg('reviews__rating')).order_by('-avg_rating')[:2]
        serializer = ProductSerializers(top_products, many=True)
        return Response(serializer.data)


    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None ):
        product = self.get_object()
        reviews = product.reviews.all()

        if reviews.count() == 0:
            return Response({"average_rating": "No reviews yet!"})

        avg_rating = sum({review.rating for review in reviews}) / reviews.count()

        return Response({'average_rating': avg_rating})
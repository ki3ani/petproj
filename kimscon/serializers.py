from rest_framework import serializers
from .models import Product, Order, Review, Analytics

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'seller', 'title', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'buyer', 'product', 'purchase_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'reviewer', 'product', 'rating', 'comment']

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['id', 'seller', 'total_sales', 'total_revenue']
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # this will include all fields in the model, but you can also specify a list of fields to include or exclude
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at']
from rest_framework import serializers
from .models import Category, Product
from account.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    my_product = UserSerializer(many=True)
    class Meta:
        model = Product
        fields = (
                "id",
                'name',
                "get_absolute_url",
                "description",
                "price",
                "get_image",
                "get_thumbnail",
                'quantity',
                'my_product'
                
            )
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
                "id",
                "name",
                "slug",
                "products",
                "get_absolute_url",
                )

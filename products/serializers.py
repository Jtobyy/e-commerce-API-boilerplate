from rest_framework import serializers, permissions

from .models import Product, Tag


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)  

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'tags',
            'regular_price',
            'sale_price',
            'weight',
            'image',
            'inventory',
            'date',
        ]

        def get_id(self, obj):
            return obj.id

class TagSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'image',
        ]

    def get_id(self, obj):
            return obj.id        


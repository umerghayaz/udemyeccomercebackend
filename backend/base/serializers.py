from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
class ProductSerializer(serializers.ModelSerializer):
    # reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
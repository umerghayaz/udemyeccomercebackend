from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

def getroutes(request):
    return JsonResponse('HELLO')
@api_view(['GET'])
def get_products(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def grt_product(request,pk):
    product=Product.objects.get(_id=pk)
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)
    # # product=None
    # # for i in products:
    # #     if i['_id']==pk:
    # #         product=i
    # #         break
    # return Response(serializer.data)
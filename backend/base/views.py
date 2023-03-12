from django.shortcuts import render
from django.http import JsonResponse
from .products import products
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

def getroutes(request):
    return JsonResponse('HELLO')
@api_view(['GET'])
def productsfunc(request):
    return Response(products)
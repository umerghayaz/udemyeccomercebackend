from django.urls import path
from . import views
urlpatterns = [
    path("", views.getroutes,name='routes'),
path("products/", views.productsfunc,name='products'),
]
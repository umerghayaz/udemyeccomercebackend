from django.urls import path
from . import views
urlpatterns = [
    path("", views.getroutes,name='routes'),
path("products/", views.get_products,name='products'),
path("products/<str:pk>", views.grt_product,name='products'),

]
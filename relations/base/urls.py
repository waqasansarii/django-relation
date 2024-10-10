from django.urls import path
from .views.category import get_create_category,get_update_delete_category
from .views.products import get_create_products

urlpatterns = [
    path('categories/', get_create_category),
    path('categories/<id>', get_update_delete_category),
    path('products/', get_create_products),
]
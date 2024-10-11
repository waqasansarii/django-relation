from django.urls import path
from .views.category import get_create_category,get_update_delete_category
from .views.products import get_create_products,get_update_delete_product
from .views.supplier import get_create_supplier,get_update_delete_supplier

urlpatterns = [
    path('categories/', get_create_category),
    path('categories/<id>', get_update_delete_category),
    path('products/', get_create_products),
    path('products/<id>', get_update_delete_product),
    path('suppliers/', get_create_supplier),
    path('suppliers/<id>', get_update_delete_supplier),
]
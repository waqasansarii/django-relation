from django.urls import path
from .views.category import get_create_category
from .views.student import get_create_student

urlpatterns = [
    path('categories/', get_create_category),
    path('students/', get_create_student),
]
from django.urls import path 
from .views import index, plantilla, blog

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('', index, name='index'),
    path('plantilla/', plantilla, name='plantilla'),
]

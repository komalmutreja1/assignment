from django.urls import path
from products.views import ProductView


"""
URL routes for Products App
"""

urlpatterns = [
    path('product/', ProductView.as_view(), name='products')
]

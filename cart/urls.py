from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.cart),
    path('cart/<int:pk>/', views.CartDetail.as_view()),
    path('add/', views.add_to_cart),
]

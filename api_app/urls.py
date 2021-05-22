from django.urls import path
from .views import ShoppingCart, ShoppingCartUpdate

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
    path('update-items/<int:item_id>', ShoppingCartUpdate.as_view()),
]
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import CartItem
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ShoppingCart(View):
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        product_name = data.get('product_name')
        product_price = data.get('product_price')
        product_quantity = data.get('product_quantity')

        product_data = {
            'product_name': product_name,
            'product_price': product_price,
            'product_quantity': product_quantity
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)


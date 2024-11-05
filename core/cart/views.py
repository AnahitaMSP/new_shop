from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .cart import CartSession

class SessionAddProduct(View):  # Inherit from View
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        return JsonResponse({"cart": cart.get_cart_items()})
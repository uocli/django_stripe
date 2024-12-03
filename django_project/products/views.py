from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

import stripe


def home(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1QRzOuC6sG47z0d5mrWTgKkG",  # Price API ID
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "products/home.html")


def success(request):
    return render(request, "products/success.html")


def cancel(request):
    return render(request, "products/cancel.html")

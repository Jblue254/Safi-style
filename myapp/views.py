from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm


def product_list(request):
    products = Product.objects.all()
    return render(
        request,
        "product_list.html",
        {"products": products}
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(
        request,
        "product_detail.html",
        {"product": product}
    )


@login_required
def order_list(request):
    orders = Order.objects.filter(
        user=request.user
    )

    return render(
        request,
        "order_list.html",
        {"orders": orders}
    )

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )
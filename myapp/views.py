from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Product, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_staff:
                return redirect("/admin/")

            return redirect("product_list")

        else:
            messages.error(
                request,
                "Invalid username or password"
            )

    return render(
        request,
        "login.html"
    )
def logout_user(request):
    logout(request)
    return redirect('/')

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
def place_order(request, pk):
    product = get_object_or_404(Product, pk=pk)

    order = Order.objects.create(
        user=request.user
    )

    OrderItem.objects.create(
        order=order,
        product=product,
        quantity=1
    )

    return redirect("order_list")


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
@login_required
def create_order(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        quantity = int(request.POST.get("quantity"))

        order = Order.objects.create(
            user=request.user
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

        return redirect("order_detail", pk=order.id)

    return render(
        request,
        "create_order.html",
        {"product": product}
    )
@login_required
def order_detail(request, pk):

    order = get_object_or_404(
        Order,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "order_detail.html",
        {"order": order}
    )
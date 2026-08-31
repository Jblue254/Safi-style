from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.product_list,
        name="product_list"
    ),

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail"
    ),

    path(
        "product/<int:pk>/order/",
        views.place_order,
        name="place_order"
    ),

    path(
        "orders/",
        views.order_list,
        name="order_list"
    ),
    path(
        "register/",
        views.register,
        name="register"
    ),
    path(
        "login/",
        views.login_user,
        name="login"
    ),
    path(
        'logout/',
        views.logout_user,
        name='logout'
    ),
    path(
        "order/create/<int:pk>/",
        views.create_order,
        name="create_order"
    ),
    path(
        "orders/<int:pk>/",
        views.order_detail,
        name="order_detail"
    ),

]
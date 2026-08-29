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
        'logout/',
        views.logout_user,
        name='logout'
    ),
    path(
        "order/create/<int:pk>/",
        views.create_order,
        name="create_order"
    ),

]
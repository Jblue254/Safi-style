from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Category, Product, Order, OrderItem


class ProductViewTest(TestCase):

    def setUp(self):
        category = Category.objects.create(
            name="Electronics"
        )

        Product.objects.create(
            name="Laptop",
            price=1000,
            category=category
        )

    def test_product_list_view(self):
        response = self.client.get("/")

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Laptop"
        )
class ProductDetailTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name="Electronics"
        )

        self.product = Product.objects.create(
            name="Laptop",
            price=1000,
            category=self.category
        )

    def test_product_detail_view(self):
        response = self.client.get(
            reverse(
                "product_detail",
                kwargs={"pk": self.product.pk}
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Laptop"
        )

    def test_product_detail_missing_product(self):
        response = self.client.get(
            reverse(
                "product_detail",
                kwargs={"pk": 9999}
            )
        )

        self.assertEqual(
            response.status_code,
            404
        )

class AuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="john",
            password="password123"
        )

    def test_user_can_login(self):

        login_successful = self.client.login(
            username="john",
            password="password123"
        )

        self.assertTrue(login_successful)

    def test_user_cannot_login_with_wrong_password(self):

        login_successful = self.client.login(
            username="john",
            password="wrongpassword"
        )

        self.assertFalse(login_successful)

    def test_anonymous_user_cannot_access_orders(self):

        response = self.client.get(
            reverse("order_list")
        )

        self.assertEqual(
            response.status_code,
            302
        )

    def test_logged_in_user_can_access_orders(self):

        self.client.login(
            username="john",
            password="password123"
        )

        response = self.client.get(
            reverse("order_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )
from django.test import TestCase
from .models import Category, Product


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
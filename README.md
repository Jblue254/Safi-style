# Safi Style

Safi Style is a Django-based e-commerce web application that allows users to browse products, view product details, authenticate into the system, and place orders.

## Author

**Name:** Japheth Kiprono
**Username:** jblue254
**Email:** [japhethkiprono2020@gmail.com](mailto:japhethkiprono2020@gmail.com)

## Features

* Product listing
* Product detail pages
* Product categories
* Product pricing in Kenyan Shillings (Ksh)
* User registration and authentication
* Login and logout
* Product ordering
* Order management
* Users can view their own orders
* Users cannot view other users' orders
* Product image uploads
* Automated Django tests

## Technologies Used

* Python
* Django 6.1
* SQLite
* HTML5
* Tailwind CSS
* Django Templates
* Pillow for image uploads

## Project Structure

```text
Safi-style/
│
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── products.html
│   │   ├── product_detail.html
│   │   ├── orders.html
│   │   └── ...
│   │
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── media/
│   └── products/
│
├── manage.py
├── requirements.txt
└── README.md
```

## Models

The application currently contains four main models.

### Category

Stores product categories.

```text
Category
├── id
└── name
```

### Product

Stores information about products.

```text
Product
├── id
├── category
├── name
├── price
└── image
```

### Order

Stores orders made by users.

```text
Order
├── id
├── user
└── created_at
```

### OrderItem

Connects products to orders and stores the quantity purchased.

```text
OrderItem
├── id
├── order
├── product
└── quantity
```

The total price of an order item is calculated using:

```text
Product Price × Quantity
```

## Installation

### 1. Clone the project

```bash
git clone <your-repository-url>
cd Safi-style
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv my-env
```

### 3. Activate the virtual environment

Windows Command Prompt:

```bash
my-env\Scripts\activate
```

PowerShell:

```bash
.\my-env\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If Pillow is not included:

```bash
pip install Pillow
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create your administrator account.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Admin Panel

The Django admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

Administrators can manage:

* Categories
* Products
* Product images
* Orders
* Order items
* Users

## Product Images

Products support image uploads using Django's `ImageField`.

Images are uploaded to:

```text
media/products/
```

The application uses:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

During development, Django serves uploaded images using the project's URL configuration.

## Authentication

Users must be authenticated before accessing their orders.

Anonymous users attempting to access the orders page are redirected to the login page.

Users can:

1. Register an account
2. Log in
3. Browse products
4. View product details
5. Buy products
6. View their orders
7. Log out

## Order Security

Orders are associated with individual users.

The application ensures that users only see their own orders.

For example:

```python
orders = Order.objects.filter(
    user=request.user
)
```

This prevents one user from seeing another user's orders.

## Testing

The project uses Django's built-in testing framework.

Run all tests with:

```bash
python manage.py test
```

The tests currently cover:

* Product listing
* Product details
* Missing products
* User login
* Invalid passwords
* Authentication requirements
* Order access
* Order ownership
* Category creation
* Product creation
* Order creation
* Order item creation
* User logout

A successful test run should look similar to:

```text
Found 14 test(s).

..............

----------------------------------------------------------------------
Ran 14 tests in 0.XXXs

OK
```

## Example Test

The project tests that users cannot see another user's orders:

```python
def test_user_cannot_see_another_users_order(self):

    self.client.login(
        username="john",
        password="password123"
    )

    response = self.client.get(
        reverse("order_list")
    )

    self.assertNotContains(
        response,
        f"Order {self.order2.id}"
    )
```

This helps protect user order privacy.

## Running the Project

Every time you work on the project:

```bash
my-env\Scripts\activate
python manage.py runserver
```

To run the tests:

```bash
python manage.py test
```

## Future Improvements

Possible future features include:

* Shopping cart
* Online payments
* Product search
* Product filtering by category
* Admin dashboard
* Order status tracking
* Product reviews and ratings
* Wishlist
* Order confirmation emails
* Improved mobile experience

## Contact

**Japheth Kiprono**

**Username:** jblue254

**Email:** [japhethkiprono2020@gmail.com](mailto:japhethkiprono2020@gmail.com)


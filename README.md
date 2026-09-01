# Safi Style

**Track Products. Place Orders. Shop Simply.**

## Project Overview

**`Safi Style`** is a Django-based e-commerce web application that allows users to browse products, view product details, create accounts, log in, place orders, and view their own orders.

The application provides a simple shopping experience where users can browse available products, select a product, specify the quantity they want, place an order, and view their order history and order details.

The project uses **`Django`** for the backend and **`Tailwind CSS`** for a modern and responsive user interface.

The application also uses Django's built-in authentication system to protect user-specific functionality such as placing orders and viewing orders.

## Problems It Solves

- **`Product Discovery:`** Allows users to easily browse available products.
- **`Manual Order Management:`** Provides a structured way for users to place and manage orders.
- **`Unauthorized Order Access:`** Prevents users from viewing orders belonging to other users.
- **`User Authentication:`** Provides registration, login, and logout functionality.
- **`Order Tracking:`** Allows users to view their previous orders and order details.
- **`Responsive Design:`** Provides a clean and user-friendly interface across different screen sizes.

## Features

- Add and manage products.
- Browse available products.
- View individual product details.
- Display product prices and categories.
- User registration.
- User login and logout.
- Authentication-protected order functionality.
- Place orders for products.
- Specify product quantities when placing orders.
- View personal order history.
- View individual order details.
- Prevent users from accessing other users' orders.
- Django admin interface for managing products, categories, orders, and order items.
- Responsive user interface using `Tailwind CSS`.
- Django template inheritance.
- `CSRF` protection on POST forms.
- Django built-in authentication.
- Git version control.
- GitHub repository and collaborative development using feature branches and pull requests.

## Project Structure

```text
safi-style/
│
├── myapp/
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   ├── create_order.html
│   │   ├── order_list.html
│   │   └── order_detail.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── safistyle/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
```

## Technologies Used

- `Python 3`
- `Django`
- `SQLite`
- `HTML5`
- `CSS3`
- `Tailwind CSS`
- `Django Forms`
- `Django Authentication`
- `Django Testing Framework`
- `Git`
- `GitHub`

## Core Django Concepts Demonstrated

- Django project and app structure
- Django models
- Django migrations
- Django views
- URL routing
- Django templates
- Template inheritance
- Django Forms
- Form validation
- User authentication
- Authorization and permissions
- Object ownership
- CRUD operations
- Django Admin
- `CSRF` protection
- Automated testing
- Django `TestCase`
- Django test client
- Git version control
- Collaborative Git workflow

## Database Models

The application uses four main models:



## How the Application Works

1. Open the Safi Style website.
2. Browse the available products.
3. Select a product to view its details.
4. Create an account or log in.
5. Select the quantity required.
6. Submit the order.
7. The application creates an `Order` associated with the logged-in user.
8. An `OrderItem` is created containing the selected product and quantity.
9. The user is redirected to their order list.
10. The user can view their previous orders.
11. The user can select an order to view its details.
12. Users can only access orders belonging to their own account.

## Authentication

Safi Style uses Django's built-in authentication system.

Users can:

- Register an account.
- Log in.
- Log out.
- Access protected order pages after authentication.

Anonymous users attempting to access protected pages are redirected to the login page.

The application uses Django's `login_required` decorator to protect views such as order creation and order history.



This prevents a user from accessing another user's order simply by changing the order ID in the URL.

For example:

```text
John → Order #1 → Allowed

Jane → Order #1 → Rejected
```

## Application Pages

### Home / Product List

The product page displays:

- Available products
- Product names
- Product prices
- Links to individual product details

### Product Detail

The product detail page displays:

- Product name
- Product price
- Product category
- Order functionality
- Continue shopping option

### Registration

The registration page allows new users to create accounts.

### Login

The login page allows registered users to authenticate.

### My Orders

The order page displays orders belonging to the currently logged-in user.

### Order Details

The order details page displays information about a specific order and its associated products.

### Admin Dashboard

The Django admin dashboard allows administrators to:

- View categories
- Add categories
- Edit categories
- Delete categories
- View products
- Add products
- Edit products
- Delete products
- View orders
- Manage order items

## Advanced Django Testing

Testing is an important part of the project.

The application uses Django's `TestCase` and test client to verify that the application behaves correctly.

The tests cover areas such as:

- Product creation.
- Category creation.
- Order creation.
- Order item creation.
- Product list access.
- Product detail access.
- Missing product handling.
- User authentication.
- Incorrect login credentials.
- Anonymous access restrictions.
- Logged-in user access.
- Order ownership.
- User logout.

The test suite also verifies that users cannot see orders belonging to other users.

Run the tests using:

```bash
python manage.py test myapp
```

The current test suite contains **`14 tests`**, all of which pass at the current stage of development.


## Security

The application follows Django security practices including:

- Django authentication.
- Authentication-protected order views.
- Object ownership checks.
- `CSRF` protection on POST forms.
- Django form validation.
- Server-side validation.
- Django's built-in password hashing.
- Protected user-specific order information.
- `POST` requests for order creation.

## Git and Collaboration

The project uses **`Git`** and **`GitHub`** for version control and team collaboration.

The team works using feature branches so that individual changes can be developed separately before being merged into the main project.

Typical workflow:

```bash
git checkout -b feature-name

git add .

git commit -m "Add new feature"

git push origin feature-name
```

A Pull Request can then be created for the team to review and merge the changes into the main branch.

The project also uses an upstream repository to synchronize changes made by other team members.

## Installation

### Prerequisites

Make sure you have the following installed:

- `Python 3.x`
- `pip`
- `Git`
- `Visual Studio Code`

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Safi-style.git
```

### Open the Project

```bash
cd Safi-style
```

Open the project in Visual Studio Code:

```bash
code .
```

## Create a Virtual Environment

On Windows:

```bash
python -m venv my-env
```

Activate the virtual environment using Git Bash:

```bash
source my-env/Scripts/activate
```

Or using Command Prompt:

```bash
my-env\Scripts\activate
```

## Install Dependencies

Install Django:

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

## Database Setup

The project currently uses Django's `SQLite` database for development.

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create an Admin Account

Create a Django superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to provide:

- Username
- Email address
- Password

## Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the application in your browser:

`http://127.0.0.1:8000/`

The Django administration panel is available at:

`http://127.0.0.1:8000/admin/`

## Future Improvements

- Shopping cart functionality.
- Product search.
- Product filtering.
- Product images.
- Product reviews and ratings.
- Payment integration.
- Order status tracking.
- Email order confirmations.
- User profile pages.
- Product stock management.
- Wishlist functionality.
- Product categories and filtering.
- REST API integration.
- API authentication.
- Automated email notifications.
- More comprehensive automated testing.
- Deployment to a production hosting platform.

## Contribution

You can contribute by:

- Improving the user interface.
- Adding new e-commerce features.
- Improving authentication and authorization.
- Improving order management.
- Improving database functionality.
- Fixing bugs.
- Improving validation.
- Adding automated tests.
- Improving documentation.
- Improving application performance.

### How to Contribute

1. Fork the repository.
2. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Safi-style.git
```

3. Create a feature branch:

```bash
git checkout -b feature-name
```

4. Make your changes.
5. Run the tests:

```bash
python manage.py test myapp
```

6. Commit your changes:

```bash
git add .
git commit -m "Add new feature"
```

7. Push your branch:

```bash
git push origin feature-name
```

8. Create a Pull Request.

## Author

**Developed by the Safi Style Team**

## License

This project is developed for educational purposes and is free to use, modify, and distribute.
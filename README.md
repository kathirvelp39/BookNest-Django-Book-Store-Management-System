# BookNest – Django Book Store Management System

## 📚 Project Overview

**BookNest** is a web-based Book Store Management System developed using Django, Python, MySQL, HTML, CSS, and Bootstrap.

The application allows users to browse books, search for books, filter by category and price, add books to a shopping cart, and place orders. It also provides administrative features for managing books, categories, inventory, orders, and sales summaries.

This project focuses on implementing a complete bookstore workflow, from user authentication and book browsing to checkout, order management, and inventory updates.

## 🎯 Project Objectives

- Develop a user-friendly online bookstore.
- Implement secure user authentication.
- Manage books and categories efficiently.
- Provide book search, filtering, and sorting.
- Implement shopping cart and checkout functionality.
- Track customer orders and order statuses.
- Maintain inventory by updating stock after successful orders.
- Provide an administrative dashboard for store management.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| MySQL | Database management |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive user interface |
| Django ORM | Database operations |
| Git and GitHub | Version control and source code hosting |

## ✨ Features

### 1. User Authentication
- User registration
- Login and logout
- User profile
- Authentication-protected pages

### 2. Book Management
- Add new books
- View book details
- Update book information
- Delete books
- Manage book prices and stock
- Upload book cover images

### 3. Category Management
- Create categories
- View categories
- Update categories
- Delete categories

### 4. Search, Filtering and Sorting
- Search books by title
- Search books by author
- Filter books by category
- Filter books by minimum and maximum price
- Sort books by title, price, and newest additions

### 5. Shopping Cart
- Add books to the cart
- Update item quantities
- Remove items from the cart
- Calculate item subtotals
- Calculate the cart total
- Validate available stock

### 6. Checkout and Order Processing
- Enter the shipping address
- Validate stock before placing an order
- Create orders and order items
- Store order item prices at the time of purchase
- Reduce book stock after successful order creation
- Clear the cart after a successful checkout

### 7. Order Management
- View order history
- View individual order details
- Track order status

Available order statuses:
- Pending
- Confirmed
- Shipped
- Delivered
- Cancelled

### 8. Admin Dashboard
The planned dashboard provides:
- Total number of books
- Total number of orders
- Sales summary
- Low-stock book list
- Links to administrative management pages

Dashboard availability and summary calculations should be verified in the running application.

### 9. Django Administration
- Manage orders
- View order items
- Search and filter orders
- Update order statuses
- Manage registered application data

## 📁 Project Structure

```text
bookstore_management/
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── books/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── categories/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── dashboard/
│   ├── views.py
│   └── urls.py
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   └── urls.py
├── shopping_cart/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   ├── accounts/
│   ├── books/
│   ├── orders/
│   ├── shopping_cart/
│   └── dashboard/
├── manage.py
├── requirements.txt
└── README.md
```

*Note: This structure represents the expected organization. Keep only files and folders that actually exist in your project.*

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the application:

- Python
- MySQL Server
- pip
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd bookstore_management
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the activation instructions appropriate for your system policy.

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Configure MySQL

Create a MySQL database for the application:

```sql
CREATE DATABASE bookstore_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Configure the database name, username, password, host, and port in `config/settings.py`, or use environment variables if the project has been configured to support them.

Make sure the configured database matches the database created above.

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

If all migration files are already included, running `python manage.py migrate` is normally sufficient.

### Step 7: Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### Step 8: Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

- Application: http://127.0.0.1:8000/
- Django Admin: http://127.0.0.1:8000/admin/
- Admin Dashboard: http://127.0.0.1:8000/dashboard/

The dashboard URL requires an authorized staff account.

## 🧪 Testing

The following workflows have been tested during development:

- Shopping cart displays the selected book, quantity, subtotal, and total.
- Checkout successfully creates an order.
- Order History displays the created order and its status.
- Order Details displays the order information and items.
- Django Admin displays order records.
- Book stock decreased from 10 to 9 after placing an order for one copy.
- Book search and filtering features were demonstrated.
- Category CRUD operations were confirmed to work.

Additional testing should verify insufficient-stock rejection, all order status transitions, staff-only dashboard access, and the complete registration-to-checkout workflow.

## 🔒 Security Considerations

- Do not commit database passwords, secret keys, or `.env` files.
- Use a strong Django secret key.
- Keep `DEBUG = False` in production.
- Configure `ALLOWED_HOSTS` for deployment.
- Use environment variables for production credentials.
- Validate form inputs and enforce authentication and authorization.
- Never deploy the development server as a production server.

## 🚀 Future Enhancements

- Online payment gateway integration
- Email order notifications
- Pagination for book listings
- Sales charts and reports
- Customer reviews and ratings
- Automated unit and integration tests
- Deployment to a production hosting platform

## 👨‍💻 Developer

**Kathirvel P**

Project: BookNest – Django Book Store Management System

## 📄 License

This project was developed for educational and learning purposes. Add a suitable license if the project is intended for public distribution.

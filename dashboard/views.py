from django.shortcuts import render

# Create your views here.

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum
from django.shortcuts import render

from books.models import Book
from orders.models import Order


@staff_member_required
def dashboard_home(request):
    total_books = Book.objects.count()
    total_orders = Order.objects.count()

    total_sales = (
        Order.objects.filter(
            status__in=["CONFIRMED", "SHIPPED", "DELIVERED"]
        ).aggregate(total=Sum("total_amount"))["total"]
        or 0
    )

    low_stock_books = Book.objects.filter(stock__lte=5).order_by("stock")

    context = {
        "total_books": total_books,
        "total_orders": total_orders,
        "total_sales": total_sales,
        "low_stock_books": low_stock_books,
    }

    return render(request, "dashboard/home.html", context)


from decimal import Decimal, InvalidOperation

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm


@login_required
def book_list(request):
    books = Book.objects.select_related("category").all()

    # Search by book title or author
    search_query = request.GET.get("q", "").strip()
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query)
            | Q(author__icontains=search_query)
        )

    # Filter by category
    category_id = request.GET.get("category", "").strip()
    if category_id.isdigit():
        books = books.filter(category_id=int(category_id))

    # Minimum price filter
    min_price = request.GET.get("min_price", "").strip()
    if min_price:
        try:
            min_value = Decimal(min_price)
            if min_value >= 0:
                books = books.filter(price__gte=min_value)
            else:
                min_price = ""
        except InvalidOperation:
            min_price = ""

    # Maximum price filter
    max_price = request.GET.get("max_price", "").strip()
    if max_price:
        try:
            max_value = Decimal(max_price)
            if max_value >= 0:
                books = books.filter(price__lte=max_value)
            else:
                max_price = ""
        except InvalidOperation:
            max_price = ""

    # Sorting
    sort_by = request.GET.get("sort", "title")
    allowed_sort_options = {
        "title": "title",
        "price_low": "price",
        "price_high": "-price",
        "newest": "-id",
    }

    if sort_by not in allowed_sort_options:
        sort_by = "title"

    books = books.order_by(allowed_sort_options[sort_by])

    # Categories for dropdown
    from categories.models import Category
    categories = Category.objects.all().order_by("name")

    context = {
        "books": books,
        "categories": categories,
        "search_query": search_query,
        "selected_category": category_id,
        "min_price": min_price,
        "max_price": max_price,
        "sort_by": sort_by,
    }

    return render(request, "books/book_list.html", context)


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "books/book_form.html",
        {"form": form, "book": book},
    )


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "books/book_confirm_delete.html", {"book": book})

from django.shortcuts import render

# Create your views here.

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from books.models import Book
from .models import CartItem


@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user).select_related(
        "book", "book__category"
    )

    total = sum((item.subtotal for item in items), start=0)

    return render(
        request,
        "shopping_cart/cart.html",
        {
            "items": items,
            "total": total,
        },
    )


@login_required
@require_POST
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if book.stock < 1:
        messages.error(request, "This book is currently out of stock.")
        return redirect("book_list")

    with transaction.atomic():
        item = CartItem.objects.select_for_update().filter(
            user=request.user,
            book=book,
        ).first()

        if item:
            if item.quantity >= book.stock:
                messages.error(request, "You cannot add more than the available stock.")
            else:
                item.quantity += 1
                item.save(update_fields=["quantity"])
                messages.success(request, "Cart quantity updated.")
        else:
            CartItem.objects.create(
                user=request.user,
                book=book,
                quantity=1,
            )
            messages.success(request, "Book added to your cart.")

    return redirect("cart_view")


@login_required
@require_POST
def update_cart_item(request, item_id):
    item = get_object_or_404(
        CartItem,
        pk=item_id,
        user=request.user,
    )

    try:
        quantity = int(request.POST.get("quantity", "1"))
    except (ValueError, TypeError):
        messages.error(request, "Please enter a valid quantity.")
        return redirect("cart_view")

    if quantity < 1:
        messages.error(request, "Quantity must be at least 1.")
    elif quantity > item.book.stock:
        messages.error(
            request,
            f"Only {item.book.stock} copies are currently available.",
        )
    else:
        item.quantity = quantity
        item.save(update_fields=["quantity"])
        messages.success(request, "Cart updated successfully.")

    return redirect("cart_view")


@login_required
@require_POST
def remove_cart_item(request, item_id):
    item = get_object_or_404(
        CartItem,
        pk=item_id,
        user=request.user,
    )
    item.delete()
    messages.success(request, "Book removed from your cart.")
    return redirect("cart_view")

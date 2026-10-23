from django.shortcuts import render

# Create your views here.

from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book
from shopping_cart.models import CartItem
from .models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):
    cart_items = list(
        CartItem.objects.filter(user=request.user).select_related("book")
    )

    if not cart_items:
        messages.error(request, "Your cart is empty.")
        return redirect("cart_view")

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    order_items = []
                    total = Decimal("0.00")

                    # Lock book rows and validate stock before creating order.
                    for item in cart_items:
                        book = Book.objects.select_for_update().get(
                            pk=item.book_id
                        )

                        if item.quantity < 1 or item.quantity > book.stock:
                            raise ValueError(
                                f"Insufficient stock for {book.title}."
                            )

                        total += book.price * item.quantity
                        order_items.append((book, item.quantity))

                    order = Order.objects.create(
                        user=request.user,
                        total_amount=total,
                        shipping_address=form.cleaned_data["shipping_address"],
                    )

                    for book, quantity in order_items:
                        OrderItem.objects.create(
                            order=order,
                            book=book,
                            book_title=book.title,
                            unit_price=book.price,
                            quantity=quantity,
                        )

                        book.stock -= quantity
                        book.save(update_fields=["stock"])

                    CartItem.objects.filter(user=request.user).delete()

            except (Book.DoesNotExist, ValueError) as error:
                messages.error(request, str(error))
                return redirect("cart_view")

            messages.success(
                request,
                f"Order #{order.pk} placed successfully!",
            )
            return redirect("order_history")

    else:
        form = CheckoutForm()

    total = sum(
        (item.book.price * item.quantity for item in cart_items),
        Decimal("0.00"),
    )

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form,
            "cart_items": cart_items,
            "total": total,
        },
    )


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "orders/order_history.html", {"orders": orders})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(
        Order.objects.prefetch_related("items"),
        pk=pk,
        user=request.user,
    )
    return render(request, "orders/order_detail.html", {"order": order})

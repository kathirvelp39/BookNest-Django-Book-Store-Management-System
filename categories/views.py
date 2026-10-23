from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import CategoryForm


@login_required
def category_list(request):
    categories = Category.objects.all().order_by("name")
    return render(
        request,
        "categories/category_list.html",
        {"categories": categories},
    )


@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    return render(
        request,
        "categories/category_form.html",
        {"form": form, "title": "Add Category"},
    )


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category_list")
    else:
        form = CategoryForm(instance=category)

    return render(
        request,
        "categories/category_form.html",
        {"form": form, "title": "Edit Category"},
    )


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        category.delete()
        return redirect("category_list")

    return render(
        request,
        "categories/category_confirm_delete.html",
        {"category": category},
    )
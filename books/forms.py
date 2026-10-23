
from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "isbn",
            "price",
            "description",
            "category",
            "stock",
            "cover_image",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter book title",
            }),
            "author": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter author name",
            }),
            "isbn": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter ISBN",
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Enter price",
                "step": "0.01",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter book description",
            }),
            "category": forms.Select(attrs={
                "class": "form-select",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
            "cover_image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }

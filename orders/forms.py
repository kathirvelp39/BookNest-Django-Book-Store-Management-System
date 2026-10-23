
from django import forms


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(
        label="Shipping Address",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Enter your full delivery address",
            }
        ),
    )

from django import forms


class PhoneForm(forms.Form):
    phone = forms.CharField(max_length=16)
    message = forms.CharField(max_length=100)

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Needed to verify your account')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text='Your password must contain at least 8 characters'

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 10:
            raise ValidationError("Password must contain 10 characters.")
        return password1
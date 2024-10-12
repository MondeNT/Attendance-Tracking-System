from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Employee

class AddEmployeeForm(UserCreationForm):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
        ('Manager', 'Manager')
    ]

    phone = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)  # Role dropdown

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'role', 'gender', 'age', 'phone', 'email', 'username', 'password1', 'password2']
        
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'your-email@example.com',
        'class': 'form-control rounded-pill py-2 px-3'
    }))

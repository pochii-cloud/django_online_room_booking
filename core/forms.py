from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['username', 'email', 'message']


class RegisterForm(UserCreationForm):
    model = User
    fields = '__all__'

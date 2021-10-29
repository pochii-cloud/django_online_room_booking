from django import forms

from core.models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['username', 'email', 'message']

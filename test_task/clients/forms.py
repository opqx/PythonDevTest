from django.forms import ModelForm
from django import forms
from clients.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'company', 'email', 'phone', 'interest']

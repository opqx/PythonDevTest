from django.forms import ModelForm
from django import forms
from clients.models import Contact, Companies, City, Street


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'interest']


class CompaniesForm(ModelForm):
    class Meta:
        model = Companies
        fields = ['company']


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']


class StreetForm(ModelForm):
    class Meta:
        model = Street
        fields = ['name']

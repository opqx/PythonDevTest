from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200) 
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

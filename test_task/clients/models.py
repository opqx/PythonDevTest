from django.db import models
from django.urls import reverse


class Companies(models.Model):
    company = models.CharField(max_length=200, unique=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.company

class Contact(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


class Country(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Country", max_length=50)

    
    def __str__(self):
        return self.name    

class Region(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Region", max_length=50)

    
    def __str__(self):
        return self.name    
    

class City(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("City", max_length=50)

    
    def __str__(self):
        return self.name    
    

class Street(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Street", max_length=50)

    
    def __str__(self):
        return self.name    
    

class Building(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    street = models.ForeignKey(Street, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Building", max_length=50)

    
    def __str__(self):
        return self.name    
    

class Office(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Office", max_length=50)

    
    def __str__(self):
        return self.name    


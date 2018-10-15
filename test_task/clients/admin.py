from django.contrib import admin
from .models import Contact, Companies, Country, Region, City, Street, Building, Office


class CountryInline(admin.StackedInline):
    model = Country


class RegionInline(admin.StackedInline):
    model = Region



class CityInline(admin.StackedInline):
    model = City


class StreetInline(admin.StackedInline):
    model = Street


class BuildingInline(admin.StackedInline):
    model = Building


class OfficeInline(admin.StackedInline):
    model = Office


class CompaniesAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['company', 'contact', 'country', 'region', 'city', 'street', 'building', 'office']
    search_fields = ['company', 'contact__name', 'country__name', 'region__name', 'city__name', 'street__name', 'building__name', 'office__name']

    
    def contact(self, obj):
        return Contact.objects.filter(company=obj.id).first()


    def country(self, obj):
        return Country.objects.filter(company=obj.id).first()


    def region(self, obj):
        return Region.objects.filter(company=obj.id).first()


    def city(self, obj):
        return City.objects.filter(company=obj.id).first()


    def street(self, obj):
        return Street.objects.filter(company=obj.id).first()


    def building(self, obj):
        return Building.objects.filter(company=obj.id).first()


    def office(self, obj):
        return Office.objects.filter(company=obj.id).first()

    
    def contact(self, obj):
        return Contact.objects.filter(company=obj.id).first()

    inlines = [CountryInline, RegionInline, CityInline, StreetInline, BuildingInline, OfficeInline]


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'email', 'phone', 'interest')
    search_fields = ['name', 'email', 'phone', 'interest']


admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.register(Country, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
admin.site.register(Street, admin.ModelAdmin)
admin.site.register(Building, admin.ModelAdmin)
admin.site.register(Office, admin.ModelAdmin)

from django.contrib import admin
from .models import Contact, Companies, Country, Region, City, Street, Building, Office

import csv
from django.http import HttpResponse

from clients.serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer


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

    actions = ["export_to_csv", "export_to_json"]

    def export_to_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields][1:5]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([ getattr(obj, field) for field in field_names[1:5] ])

        return response

    export_to_csv.short_description = "экспорт в csv"

    def export_to_json(self, request, queryset):

        meta = self.model._meta

        response = HttpResponse(content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(meta)

        serializer = ContactSerializer(queryset, many=True)
        content = JSONRenderer().render(serializer.data)
        response.write(content)

        return response

    export_to_json.short_description = "экспорт в json"

    
admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.register(Country, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
admin.site.register(Street, admin.ModelAdmin)
admin.site.register(Building, admin.ModelAdmin)
admin.site.register(Office, admin.ModelAdmin)

from django.contrib import admin
from .models import Contact, Companies, Country, Region, City, Street, Building, Office

import csv
from django.http import HttpResponse

from clients.serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer

from django.urls import path
from django.shortcuts import redirect

from io import StringIO
from clients.forms import ContactForm, CompaniesForm, CityForm, StreetForm
import json

import requests
from django.contrib import messages

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

    change_list_template = "clients/import.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('tocsv/', self.tocsv),
            path('tojson/', self.tojson),
            path('fromurl/', self.fromurl),
        ]
        return my_urls + urls

    def tocsv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["tocsv"].read()
            reader = csv.reader(StringIO(csv_file.decode("utf-8")))

            for i in reader:
                res = {'name': i[0], 'email': i[1], 'phone': i[2], 'interest': i[3]}
                form = ContactForm(res)
                if form.is_valid():
                    Contact.objects.get_or_create(name=i[0], email=i[1], phone=i[2], interest=i[3])

            self.message_user(request, "Файл csv был импортирован")
            return redirect("..")

    def tojson(self, request):
        if request.method == "POST":
            json_file = request.FILES["tojson"].read()
            reader = json.loads(json_file)

            for i in reader:
                res = {'name': i['name'], 'email': i['email'], 'phone': i['phone'], 'interest': i['interest']}
                form = ContactForm(res)
                if form.is_valid():
                    Contact.objects.get_or_create(name=i['name'], email=i['email'], phone=i['phone'], interest=i['interest'])

            self.message_user(request, "Файл json был импортирован")
            return redirect("..")


    def fromurl(self, request):
        if request.method == "POST":
            url = request.POST.get('fromurl')
            if url == '':
                return redirect("..")

            try:
                r = requests.get(url)
            except:
                messages.error(request, "неверная ссылка или сервер неотвечает")
                return redirect("..")
                

            for i in r.json():

                company = {'company': i['company']['name']}
                form = CompaniesForm(company)
                if form.is_valid():
                    id = Companies(company=i['company']['name'])
                    id.save()
                else:
                    id = Companies.objects.get(company=i['company']['name'])

                contact = {
                    'name': i['name'],
                    'email': i['email'],
                    'phone': i['phone'],
                    'interest': i['company']['bs']
                }
                form = ContactForm(contact)
                if form.is_valid():
                    contact_id = Contact.objects.get_or_create(
                        company=id,
                        name=i['name'],
                        email=i['email'],
                        phone=i['phone'],
                        interest=i['company']['bs']
                    )

                city = {
                    'name': i['address']['city'],
                }
                form = CityForm(city)
                if form.is_valid():
                    city_id = City(
                        company=id,
                        name=i['address']['city']
                    )
                    city_id.save()
                else:
                    try:
                        city_id = City.objects.get(company=i['address']['city'])
                    except:
                        city_id = None

                if city_id is not None:
                    street = {
                        'name': i['address']['street'],
                    }
                    form = StreetForm(street)
                    if form.is_valid():
                        street_id = Street.objects.get_or_create(
                            company=id,
                            city=city_id,
                            name=i['address']['street']
                        )
                else:
                    continue
                

            self.message_user(request, "данные по ссылке были импортированны")
            return redirect("..")

    
    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields][2:6]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([ getattr(obj, field) for field in field_names ])

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

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
    list_display = ['company', 'new_col', ]
    
    def new_col(self, obj):
        return "add_new_col"

    inlines = [CountryInline, RegionInline, CityInline, StreetInline, BuildingInline, OfficeInline]


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'company', 'email', 'phone', 'interest')
    search_fields = ['name', 'company', 'email', 'phone', 'interest']


admin.site.register(Companies, CompaniesAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.register(Country, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
admin.site.register(Street, admin.ModelAdmin)
admin.site.register(Building, admin.ModelAdmin)
admin.site.register(Office, admin.ModelAdmin)

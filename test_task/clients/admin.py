from django.contrib import admin
from .models import Contact


# admin.site.register(Contact)


class ContactAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('name', 'company', 'email', 'phone', 'interest')
    search_fields = ['name', 'company', 'email', 'phone', 'interest']


admin.site.register(Contact, ContactAdmin)

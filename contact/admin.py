from django.contrib import admin
from .models import Contact


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_viewed')
    list_display_links = ('id', 'name', 'email', 'phone',)
    search_fields = ('name', 'email', 'phone',)
    list_filter = ('name', 'email', 'phone',)


admin.site.register(Contact, ContactAdmin)


from django.contrib import admin
from .models import Location, Profile

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address_1', 'city', 'state', 'zip_code')
    list_filter = ('state',)
    search_fields = ('address_1', 'city', 'zip_code')
    fieldsets = (
        (None, {
            'fields': ('address_1', 'address_2')
        }),
        ('Location Details', {
            'fields': ('city', 'state', 'zip_code')
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)  # ✅ Show only "username's Profile"
    search_fields = ('user__username',)
from django.contrib import admin

# Register your models here.

from .models import Location, Bed, Client, AllocationRequest, BedClientAllocations
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'view_beds_link')

    search_fields = ['name', 'street', 'city', ]

    def view_beds_link(self, obj):
        count = obj.bed_set.count()
        print("count: ", count)
        url = (
            reverse("admin:cura_app_bed_changelist")
            + "?"
            + urlencode({"location__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Beds</a>', url, count)

    view_beds_link.short_description = "Beds"


@admin.register(Bed)
class BedsAdmin(admin.ModelAdmin):
    list_display = ('bed_number', 'location')
    list_filter = ('location',)
    # list_display_links = ('location', )
    # list_editable = ('bed_number', )

    search_fields = ['bed_number', 'location__name']


@admin.register(Client)
class ClientsAdmin(admin.ModelAdmin):
    # list_display = ('bed_number', 'location')
    # list_filter = ('location',)
    # list_display_links = ('location', )
    # list_editable = ('bed_number', )
    change_form_template = 'admin/custom_template.html'

    search_fields = ['name']


@admin.register(AllocationRequest)
class AllocationRequestAdmin(admin.ModelAdmin):

    def locations(self, obj):
        print(obj.preferred_locations.all())
        return ", ".join([location.name for location in obj.preferred_locations.all()])

    list_display = ('client', 'allocation_start_date', 'locations')
    # list_filter = ('locations',)
    # list_display_links = ('location', )
    # list_editable = ('bed_number', )


@admin.register(BedClientAllocations)
class BedClientAllocationsAdmin(admin.ModelAdmin):

    list_display = ('bed', 'client', 'allocation_start_date', 'allocation_end_date')
    # list_filter = ('locations',)
    # list_display_links = ('location', )
    # list_editable = ('bed_number', )



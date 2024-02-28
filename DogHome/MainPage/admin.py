from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'weight', 'height', 'description', 'owner', 'age', 'color', 'get_photo',
                    'breed',
                    'health', 'shelter')
    list_editable = ('owner',)
    list_display_links = ('id', 'name')
    list_filter = ('name',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниматюра'


class ShelterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_creation', 'number_of_animals', 'description', 'get_photo', 'address',
                    'contacts',
                    'contact_person',)
    list_display_links = ('id', 'name')
    list_filter = ('name',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниматюра'


class ShelterPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'shelter', 'image', 'description')
    list_display_links = ('id', 'shelter')
    list_filter = ('shelter',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title', 'description', 'photo', 'shelter')
    list_display_links = ('id', 'name')


admin.site.register(ShelterPhoto, ShelterPhotoAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Breed)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Health)

admin.site.site_title = 'DogHome'
admin.site.site_header = 'DogHome'

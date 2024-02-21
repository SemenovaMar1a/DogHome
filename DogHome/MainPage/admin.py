from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'weight', 'height', 'description', 'owner', 'age', 'color', 'photo',
                    'breed',
                    'health', 'shelter')
    list_editable = ('owner',)
    list_display_links = ('id', 'name')
    list_filter = ('name',)


class ShelterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_of_creation', 'number_of_animals', 'description', 'photo', 'address',
                    'contacts',
                    'contact_person',)
    list_display_links = ('id', 'name')
    list_filter = ('name',)


class ShelterPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'shelter', 'image', 'description')
    list_display_links = ('id', 'shelter')
    list_filter = ('shelter',)


admin.site.register(ShelterPhoto, ShelterPhotoAdmin)
admin.site.register(Dog, DogAdmin)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Breed)
admin.site.register(Employee)
admin.site.register(Health)

admin.site.site_title = 'DogHome'
admin.site.site_header = 'DogHome'

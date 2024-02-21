from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('dog_cards/', DogCard.as_view(), name='dogCards'),
    path('shelter/', ShelterCard.as_view(), name='shelterDog'),
    path('dog_cards/<int:pk>', ViewDog.as_view(), name='viewdog'),
    path('dog_cards/filter/<int:shelter_id>', DogCard.as_view(), name='shelterbydogs'),
    path('shelter/<int:pk>', ViewShelter.as_view(), name='viewshelter'),
]

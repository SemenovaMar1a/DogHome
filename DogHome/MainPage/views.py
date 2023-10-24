from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Shelter, Dog


class Main(ListView):
    model = Shelter
    template_name = 'MainPage/home_main_list.html'
    context_object_name = 'shelter'


class DogCard(ListView):
    model = Dog
    template_name = 'MainPage/dog_card_list.html'
    context_object_name = 'dogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unique_shelters'] = Shelter.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        shelter_id = self.kwargs.get('shelter_id')
        if shelter_id:
            queryset = queryset.filter(shelter_id=shelter_id)
        return queryset


class ShelterCard(ListView):
    model = Shelter
    template_name = 'MainPage/shelter_card_list.html'
    context_object_name = 'shelters'


# def index(request):
#     cart = Shelter.objects.all()
#     return render(request, 'MainPage/home_main_list.html', {'cart': cart})

class ViewDog(DetailView):
    model = Dog
    context_object_name = 'dog_item'
    template_name = 'MainPage/view_dog_list.html'


class ShelterByDogs(ListView):
    model = Dog
    template_name = 'MainPage/shelter_id_list.html'
    context_object_name = 'dogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unique_shelters'] = Shelter.objects.all()
        shelter_id = self.kwargs.get('shelter_id')
        if shelter_id:
            selected_shelter = get_object_or_404(Shelter, id=shelter_id)
            context['selected_shelter'] = selected_shelter
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        shelter_id = self.kwargs.get('shelter_id')
        if shelter_id:
            queryset = queryset.filter(shelter_id=shelter_id)
        return queryset


class ViewShelter(DetailView):
    model = Shelter
    template_name = 'MainPage/view_shelter_list.html'
    context_object_name = 'shelters'


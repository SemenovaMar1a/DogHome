from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Shelter, Dog, ShelterPhoto, Employee


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

        query = self.request.GET.get('q')
        if query:
            queryset = Dog.objects.filter(Q(name__icontains=query))
        return queryset


class ShelterCard(ListView):
    model = Shelter
    template_name = 'MainPage/shelter_card_list.html'
    context_object_name = 'shelters'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = Shelter.objects.filter(Q(name__icontains=query))
        return queryset


class ViewDog(DetailView):
    model = Dog
    context_object_name = 'dog_item'
    template_name = 'MainPage/view_dog_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            dog = self.get_object()
            context['shelter'] = dog.shelter
        except Dog.DoesNotExist:
            raise Http404("Dog does not exist")

        return context


class ViewShelter(DetailView):
    model = Shelter
    template_name = 'MainPage/view_shelter_list.html'
    context_object_name = 'shelters'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shelter_id = self.kwargs.get('pk')
        shelter_photos = ShelterPhoto.objects.filter(shelter_id=shelter_id)
        context['shelter_photos'] = shelter_photos
        return context


class HelpForShelter(ListView):
    model = Employee
    template_name = 'MainPage/help_for_shelters_list.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            employees = self.get_queryset()
            if employees.exists():
                employee_instance = employees[0]
                context['shelter'] = employee_instance.shelter
            else:
                raise Http404("No employees found")
        except Employee.DoesNotExist:
            raise Http404("Employee does not exist")

        return context


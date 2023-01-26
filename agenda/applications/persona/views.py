from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import Person
from rest_framework.generics import ListAPIView
from .serializers import PersonSerializer

class PersonListView(ListView):
    model = Person
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    queryset = Person.objects.all()

class PersonListAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonView(TemplateView):
    template_name = "persona/lista.html"

class PersonSearchAPIView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        if kword: 
            return Person.objects.filter(full_name__icontains=kword) 
        else: 
            return Person.objects.all()
    
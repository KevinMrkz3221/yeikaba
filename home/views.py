from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Service, Project

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['services'] = Service.objects.all()


        return context

from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Service, Project

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['services'] = Service.objects.all()


        return context


class WorkDetailView(DetailView):
    template_name = 'home/portfolio-details.html'
    model = Project
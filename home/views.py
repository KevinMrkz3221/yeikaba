from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Service, Project, ProjectImages

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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Obtén el proyecto actual desde el contexto
        project = context['object']

        # Obtén todas las imágenes asociadas al proyecto
        context['images'] = ProjectImages.objects.filter(project=project)


        return context
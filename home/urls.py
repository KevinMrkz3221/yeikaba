from django.urls import path
from .views import HomeView, WorkDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('work/<int:pk>', WorkDetailView.as_view(), name='work')
]

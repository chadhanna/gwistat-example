from django.urls import path
from . import views

app_name = 'detector_ranges'

urlpatterns = [
    path('', views.home, name='home'),
]
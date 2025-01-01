from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('event/', event_view, name='event_create'),            # Create mode
    path('event/<slug:slug>/', event_view, name='event_update') # View/Edit mode
]

from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('events_custom/', EventCustomListView.as_view(), name='events_custom'),
    path('events/', events, name='events'),
    path('event/', event_view, name='event_create'),            # Create mode
    path('event/<slug:slug>/', event_view, name='event_view'), # View/Edit mode
    path('event/<slug:slug>/delete', delete_event, name='delete_event') 
]

from .models import Event
from django.shortcuts import get_object_or_404, redirect, render

from events.forms import EventForm


def home(request):
    return render(request, 'home.html')

def event_view(request, slug=None):
    """
    Handles both create (no slug) and view/edit (with slug) of Event objects.
    """
    if slug:
        event_instance = get_object_or_404(Event, slug=slug)
    else:
        event_instance = None

    if request.method == 'POST':
        # Submitting the form (Create or Update)
        form = EventForm(request.POST, instance=event_instance)
        if form.is_valid():
            saved_event = form.save()
            return redirect('event_update', slug=saved_event.slug)
    else:
        # GET request: render empty form (create) or filled form (view)
        form = EventForm(instance=event_instance)

    return render(request, 'event.html', {
        'form': form,
        'event': event_instance,
    })

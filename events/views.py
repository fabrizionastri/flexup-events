#  ------- events/events/views.py 
from core.utils.print_context import _print_context
from .models import Event
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from events.forms import EventForm
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST


def events(request):
    columns = [
        {"name": "name", "title": "Title"},
        {"name": "start_datetime", "title": "Start date & time"},
        {"name": "end_datetime", "title": "End date & time"},
        {"name": "description", "title": "Description"},
        {"name": "location", "title": "Location"},
        {"name": "slug", "title": "Slug"},
    ]
    # returns a list of dictionaries containing the name and verbose name of each field in the Events model
    # columns = [{"name": field.name, "title": field.verbose_name} for field in Event._meta.fields]

    data = list(Event.objects.all())
    print("Events data:\n", data)
    context = {"title": "Events", "columns": columns, "data": data}

    return render(request, "events.html", context)

@require_POST
def delete_event(request, slug):
    print("Deleting event with slug:", slug)
    event_instance = get_object_or_404(Event, slug=slug)
    _print_context(event_instance, "slug")
    event_instance.delete()
    redirect_url = '/events/'
    print(f"Redirecting to: {redirect_url}")
    return HttpResponseRedirect(redirect_url)


def home(request):
    return render(request, 'home.html')

class EventCustomListView(ListView):
    model = Event
    template_name = 'events_custom.html'   # you can name this file whatever you want
    context_object_name = 'events'       # default is "object_list"


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
            return redirect('events')
    else:
        # GET request: render empty form (create) or filled form (view)
        form = EventForm(instance=event_instance)

    return render(request, 'event.html', {
        'form': form,
        'event': event_instance,
    })

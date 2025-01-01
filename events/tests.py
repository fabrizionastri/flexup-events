
from django.test import TestCase

from core.utils.aware_datetime import aware_datetime
from core.utils.print_context import _print_context, print_context_decorator
from .models import Event
from uuid import uuid4
from django.utils.text import slugify
from datetime import datetime, timedelta

# FILE: events/test_models.py

@print_context_decorator
class TestEventModel(TestCase):

    def test_01_slug_is_auto_generated(self):
        event = Event.objects.create(
            name="Test Event",
            start_datetime=aware_datetime("2024-12-31 09:00:00"),
            end_datetime=aware_datetime("2024-12-31 12:00:00"),
            description="Test Description",
            location="Test Location"
        )
        self.assertIsNotNone(event.slug)
        _print_context(event.slug)
        _print_context(event.duration)



    # def test_02_duration_property(self):
    #     start_time = aware_datetime(datetime.now())
    #     end_time = aware_datetime(start_time + timedelta(hours=2))
    #     event = Event.objects.create(
    #         name="Test Event",
    #         start_datetime=start_time,
    #         end_datetime=end_time,
    #         description="Test Description",
    #         location="Test Location"
    #     )
    #     self.assertEqual(event.duration, timedelta(hours=2))

    # def test_03_str_representation(self):
    #     event = Event.objects.create(
    #         name="Test Event",
    #         start_datetime=datetime.now(),
    #         end_datetime=datetime.now() + timedelta(hours=1),
    #         description="Test Description",
    #         location="Test Location"
    #     )

from django.test import TestCase
from .models import Event, Meeting
from django.urls import reverse

# Create tests here.
class MeetingsTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='weekly meeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')

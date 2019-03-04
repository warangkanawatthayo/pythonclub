from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

# Create tests here.
class MeetingsTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='weekly meeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource = Resource(resourcename = 'Resource Url')
        self.assertEqual(str(resource), resource.resourcename)
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event = Event(eventtitle = 'Test Event Title')
        self.assertEqual(str(event), event.eventtitle)
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class MinutesTest(TestCase):
    #def test_stringOutput(self):
        #minutes = MeetingMinutes(minutestime = 10)
        #self.assertEqual(str(minutes), minutes.minutestime)
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'minutes')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')

class TestGetMeetings(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertTemplateUsed(response, 'club/meetings.html')

class TestResources(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertTemplateUsed(response, 'club/resources.html')
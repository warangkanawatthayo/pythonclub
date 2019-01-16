from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Meeting, meeting minutes, resource, event

class Meeting(models.Model):
    meetingtitle = models.CharField(max_length = 255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    meetinglocation = models.CharField(max_length = 255)
    meetingagenda = models.TextField()

    def __str__(self):
        return self.meetingtitle
    
    class Meta:
        db_table = 'meeting'

class MeetingMinutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
    minutesattendance = models.ManyToManyField(User)
    minutestime = models.SmallIntegerField()

    def __str__(self):
        return self.minutestime

    class Meta:
        db_table = 'minutes'

class Resource(models.Model):
    resourcename = models.CharField(max_length = 255)
    resourcetype = models.CharField(max_length = 255)
    resourceurl = models.URLField(null = True, blank = True)
    resourcedateentered = models.DateField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resourcedescription = models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table = 'resource'

class Event(models.Model):
    eventtitle = models.CharField(max_length = 255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventlocation = models.CharField(max_length = 255)
    eventdescription = models.TextField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
db_table = 'event'

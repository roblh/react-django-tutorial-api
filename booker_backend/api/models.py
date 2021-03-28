from django.db import models
from django.contrib.auth.models import User



# Users is already handled by django
# class Users(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.TextField(max_length=360)


# # Considering removing
# class UserGroup(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     userGroupName = models.CharField(max_length=32)
#     userGroupNameDescription = models.TextField(max_length=360)



# Event Name proposals submitted by an active event's participants
class EventNames(models.Model):
    name = models.CharField(max_length=32)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

#    def return_first_highest_voted(self): 

# Create your models here.
class EventParticipants(models.Model):
    attendee = models.ManyToManyField(User,blank=True)
    userAdmitted = models.BooleanField(default=False)
    eventAdmin = models.BooleanField(default=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

#    def return_highest_voted(self): 

# Create your models here.
class EventTimes(models.Model):
    time = models.DateTimeField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

#    def return_highest_voted(self): 
#    def return_2nd_highest_voted(self): 
#    def return_3rd_highest_voted(self): 

# Create your models here.
class EventLocations(models.Model):
    location = models.CharField(max_length=32)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

#    def return_highest_voted(self): 

# Create your models here.
class Events(models.Model):
    finalEventName = models.CharField(max_length=32)
    finalEventParticipants=  models.ForeignKey(User, through='EventParticipants')
    finalEventTime= models.CharField(max_length=32)
    finalEventLocation= models.CharField(max_length=32)
    votingClosed = models.BooleanField(default=False)


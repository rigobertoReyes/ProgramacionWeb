from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
# Create your models here.

class Player(models.Model):
	name = models.CharField(max_length=50)
	number = models.IntegerField()
	position = models.CharField(max_length=3)
	weight = models.IntegerField()
	age = models.IntegerField()


	def __unicode__(self): 
		return str(self.content)

class Team(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)


	def __unicode__(self): 
		return str(self.content)

class Stadium(models.Model):
	name = models.CharField(max_length=50)
	seatcap = models.IntegerField()
	location = models.CharField(max_length=50)


	def __unicode__(self): 
		return str(self.content)
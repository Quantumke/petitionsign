from django.db import models

# Create your models here.
class petition(models.Model):
	firstname = models.CharField(max_length=100, unique=False)
	lastname = models.CharField(max_length=100, unique=False)
	date = models.DateField(max_length=100, unique =False)

	def __unicode__(self):
		return '%s' %self.firstname

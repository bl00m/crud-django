from django.db import models

# Create your models here.
class User(models.Model):
	firstname = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 50, blank=True)
	email = models.EmailField()

	def __unicode__(self):
		return self.firstname + " " + self.lastname
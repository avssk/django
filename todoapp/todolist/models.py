from django.db import models

# Create your models here.

class todo(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=500)
	created = models.DateTimeField()

	def __str__(self):
		return self.name
from django.db import models

# Create your models here.

class todo(models.Model):
	name = models.CharField(max_length=100, unique=True)
	description = models.TextField()
	created = models.DateTimeField()

	def __str__(self):
		return self.name
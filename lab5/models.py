from django.db import models

# Create your models here.
class Content(models.Model):
	content = models.CharField(max_length=60)

	def __str__(self):
	 return self.content
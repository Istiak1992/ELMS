from django.db import models

# Create your models here.

class Course(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	active_status = models.BooleanField(default=True)
	start_date = models.DateTimeField(auto_now=False)
	end_date = models.DateTimeField(auto_now=False)
	
	def __str__(self):
		return self.title

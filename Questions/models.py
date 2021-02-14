from django.db import models
from Lessons.models import Lesson

# Create your models here.

class Question(models.Model):
	question = models.CharField(max_length=1000)
	point = models.DecimalField(decimal_places=2, max_digits=10000)
	answer = models.CharField(max_length=1000)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
	first_choice = models.CharField(max_length=1000, default='First Possible Answer')
	second_choice = models.CharField(max_length=1000, default='Second Possible Answer')
	third_choice = models.CharField(max_length=1000, default='Third Possible Answer')
	fourth_choice = models.CharField(max_length=1000, default='Fourth Possible Answer')

	def __str__(self):
		return self.question

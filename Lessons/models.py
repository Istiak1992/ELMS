from django.db import models
from Courses.models import Course


class Lesson(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	active_status = models.BooleanField(default=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return f'"{self.title}" lesson from   {self.course.title} Course'

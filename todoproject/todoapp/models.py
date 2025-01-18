from django.db import models


class Task(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	priority = models.IntegerField(default=2)

	def __str__(self):
		return self.title

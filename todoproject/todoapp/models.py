from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
	description = models.TextField()
	done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	priority = models.IntegerField(default=2)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-created_at']

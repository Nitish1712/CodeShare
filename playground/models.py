from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Coder(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	code = models.TextField(default="", blank=True)

	def get_absolute_url(self):
		return reverse('home1',kwargs={'name':self.user.username})
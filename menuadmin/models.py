from django.db import models
from decimal import *

class MenuItem(models.Model):
	name = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=100, decimal_places=2)
	description = models.TextField()

	def __str__(self):
		return self.name

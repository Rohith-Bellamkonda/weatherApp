from django.db import models

# Create your models here.
class CityNames(models.Model):
	cities = models.TextField(max_length=100)
	def __str__(self):
		return self.cities
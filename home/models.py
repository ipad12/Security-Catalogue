from django.db import models

# Create your models here.

class Generic(models.Model):
	generic_name = models.CharField(max_length=200)
	generic_desc = models.TextField

	def __str__(self):
		return self.generic_name

class Solution(models.Model):
	solution_name = models.CharField(max_length=200)
	solution_desc = models.TextField
	

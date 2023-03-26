'''from django.db import models


# Create your models here.
class Attende(models.Model):
	id_number = models.CharField(max_length=10)
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)'''
	
	

from django.db import models
from django.utils import timezone
class Student(models.Model):
	RedgNo = models.CharField(max_length=10)
	M3 = models.CharField(max_length=10)
	DMS = models.CharField(max_length=10)
	DBMS = models.CharField(max_length=10)
	CO = models.CharField(max_length=10)
	OOP = models.CharField(max_length=10)
	DBMSLAB = models.CharField(max_length=10)
	OOPLAB = models.CharField(max_length=10)
	RLAB = models.CharField(max_length=10)
	WADFSLAB = models.CharField(max_length=10)
	#SGPA = models.CharField(max_length=10)
	SGPA = models.DecimalField(max_digits=5, decimal_places=2)

'''class Attende(models.Model):
	RedgNo = models.CharField(max_length=10)	
	date = models.DateField(auto_now_add=True)
	time = models.TimeField(auto_now_add=True)'''
	
	#def __str__(self):
		#return self.RedgNo

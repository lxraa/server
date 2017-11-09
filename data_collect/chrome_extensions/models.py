from django.db import models



# Create your models here.

class Employee(models.Model):
	mis = models.TextField(u'mis',default = '')
	anonymous = models.TextField(u'anonymous',default = '')
	time = models.TextField(u'time',default = '')
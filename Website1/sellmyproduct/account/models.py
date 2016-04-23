from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Contactus(models.Model):
	  name =models.CharField(max_length=200)
	  email=models.CharField(max_length=200)
	  Query=models.CharField(max_length=200)


class Forgetpass(models.Model):
	token=models.CharField(max_length=500)
	user=models.ForeignKey(User)

class Addprod(models.Model):
	category=models.CharField(max_length=500)
	title=models.CharField(max_length=500)
	desc=models.CharField(max_length=500)
	name=models.CharField(max_length=500)
	email=models.CharField(max_length=500)



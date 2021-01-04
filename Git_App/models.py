from django.db import models

# Create your models here.

class Emp(models.Model):
  eno = models.CharField(max_length=30)

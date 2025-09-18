from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=25)
    message = models.CharField(max_length=2500)

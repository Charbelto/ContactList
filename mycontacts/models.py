from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200) 
    profession = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
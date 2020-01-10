from django.db import models

# Create your models here.

class createresume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    objective = models.TextField()
    experiance = models.IntegerField()
    organization = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return self.first_name
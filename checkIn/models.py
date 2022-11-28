from django.db import models

# Create your models here.
class iDCards(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

class DateTime(models.Model):
    timeIn = models.DateTimeField("Checked In")
    timeOut = models.DateTimeField("Checked Out")

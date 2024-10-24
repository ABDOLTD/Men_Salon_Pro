from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer_name} - {self.service}'

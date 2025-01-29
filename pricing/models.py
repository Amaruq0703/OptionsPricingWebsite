from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class User(AbstractUser):
    pass

class Calculation(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="calculations")
    model = models.CharField(max_length=15, choices=[('BLACK_SCHOLES', 'Black-Scholes'), ('BINOMIAL', 'Binomial')])
    timestamp = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField()
    strike = models.IntegerField()
    expiry = models.IntegerField()
    rfr = models.IntegerField()
    vol = models.IntegerField()

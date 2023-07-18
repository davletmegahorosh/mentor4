from django.db import models
from django.contrib.auth.models import User
class Pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=128)
    price = models.IntegerField()

class Comments_pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
from django.db import models

class Pizza(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=128)
    price = models.IntegerField()

class Comments_pizza(models.Model):
    text = models.TextField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
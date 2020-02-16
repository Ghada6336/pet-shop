from django.db import models

class Petshop(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    available=models.BooleanField(default=True)

    image=models.ImageField(null=True, blank=True)
    price =models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name

from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.name
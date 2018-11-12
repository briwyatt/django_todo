from django.db import models


class Restaurants(models.Model):
    text = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text

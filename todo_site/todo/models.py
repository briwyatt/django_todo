from django.db import models


class Restaurant(models.Model):
    text = models.CharField(max_length=100)
    visited = models.BooleanField(default=False)
    comment = models.CharField(max_length=280)

    def __str__(self):
        return self.text

from django.db import models


class Textshearing(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    urls = models.CharField(max_length=100)
    def __str__(self):
        return self.urls

    
from django.db import models


class Url(models.Model):
    original_url = models.CharField("URL",max_length=1000)
    short_url = models.CharField(max_length=50)

    def __str__(self):
        return self.original_url 


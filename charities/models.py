from django.db import models


class Charity(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

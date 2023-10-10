from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    name_url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=255)

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.name_url:
            return reverse(self.name_url)
        return '#'

    def __str__(self):
        return self.title

from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_ancestors(self):
        ancestors = []
        current_item = self.parent
        while current_item is not None:
            ancestors.insert(0, current_item)
            current_item = current_item.parent
        return ancestors

    def get_children(self):
        return MenuItem.objects.filter(parent=self)
    
    def get_absolute_url(self):
        """ Returns a sting url formatted like this: /url/ """
        if self.url:
            return self.url
        return '#'
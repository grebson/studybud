from django.db import models

# Create your models here.
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True, null = True)
    # participants = 
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

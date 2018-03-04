from django.db import models

# Create your models here.
class Light(models.Model):
    state = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

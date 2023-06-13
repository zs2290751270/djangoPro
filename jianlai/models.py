from django.db import models

# Create your models here.


class Wsb(models.Model):

    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    class Meta:
        db_table = 'Wsb'

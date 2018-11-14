from django.db import models

# Create your models here.

class Planes1(models.Model):
    s = models.CharField(max_length=100, blank=True, null=True)
    p = models.CharField(max_length=200, blank=True, null=True)
    o = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planes1'

from django.db import models

# Create your models here.

"""
class Planes1(models.Model):
    s = models.CharField(max_length=100, blank=True, null=True)
    p = models.CharField(max_length=200, blank=True, null=True)
    o = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        #default_related_name = 'planes'
        verbose_name = "Planes"
        verbose_name_plural = "Planes"
        db_table = 'planes1'
"""


class Planes(models.Model):
    id = models.AutoField(primary_key=True)
    s = models.CharField(max_length=400, blank=True, null=True)
    p = models.CharField(max_length=400, blank=True, null=True)
    o = models.TextField(blank=True, null=True)

    class Meta:
        default_related_name = 'planes'
        verbose_name = "Planes"
        verbose_name_plural = "Planes"
        db_table = 'planes1'

    def __str__(self):
        return self.o

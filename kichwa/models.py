from django.db import models

# Create your models here.

class CastellanoKichwa(models.Model):
    castellano = models.CharField(max_length=125, blank=True, null=True)
    tipo = models.CharField(max_length=55, blank=True, null=True)
    kichwa = models.CharField(max_length=325, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'castellano_kichwa'


class Expresiones(models.Model):
    castellano = models.CharField(max_length=245, blank=True, null=True)
    kichwa = models.CharField(max_length=245, blank=True, null=True)
    tipo = models.ForeignKey('Tipos', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expresiones'


class KichwaCastellano(models.Model):
    kichwa = models.CharField(max_length=225, blank=True, null=True)
    phonema = models.CharField(max_length=225, blank=True, null=True)
    tipo = models.CharField(max_length=225, blank=True, null=True)
    toponimo = models.CharField(max_length=225, blank=True, null=True)
    sinonimos = models.CharField(max_length=225, blank=True, null=True)
    castellano = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kichwa_castellano'


class Multilenguaje(models.Model):
    kichwa = models.CharField(max_length=125)
    english = models.CharField(max_length=125)
    spanish = models.CharField(max_length=125)
    speech = models.CharField(max_length=85)
    category = models.CharField(max_length=215)

    class Meta:
        managed = False
        db_table = 'multilenguaje'


class Tipos(models.Model):
    castellano = models.CharField(max_length=245, blank=True, null=True)
    kichwa = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos'

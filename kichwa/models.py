from django.db import models


"""
 TODO anadir el metodo to string en todos las tablas
    def __str__(self):
        return self.nombrecampo

"""
# Create your models here.

class CastellanoKichwa(models.Model):
    castellano = models.CharField(max_length=125, blank=True, null=True)
    tipo = models.CharField(max_length=55, blank=True, null=True)
    kichwa = models.CharField(max_length=325, blank=True, null=True)

    class Meta:
        db_table = 'castellano_kichwa'


class Expresiones(models.Model):
    castellano = models.CharField(max_length=245, blank=True, null=True)
    kichwa = models.CharField(max_length=245, blank=True, null=True)
    tipo = models.ForeignKey('Tipos', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'expresiones'


class KichwaCastellano(models.Model):
    kichwa = models.CharField(max_length=225, blank=True, null=True)
    phonema = models.CharField(max_length=225, blank=True, null=True)
    tipo = models.CharField(max_length=225, blank=True, null=True)
    toponimo = models.CharField(max_length=225, blank=True, null=True)
    sinonimos = models.CharField(max_length=225, blank=True, null=True)
    castellano = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        db_table = 'kichwa_castellano'


class Multilenguaje(models.Model):
    kichwa = models.CharField(max_length=125)
    english = models.CharField(max_length=125)
    spanish = models.CharField(max_length=125)
    speech = models.CharField(max_length=85)
    category = models.CharField(max_length=215)

    class Meta:
        db_table = 'multilenguaje'


class Tipos(models.Model):
    castellano = models.CharField(max_length=245, blank=True, null=True)
    kichwa = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        db_table = 'tipos'

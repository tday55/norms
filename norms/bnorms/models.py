from django.db import models

# Create your models here.

class Boyd3(models.Model):
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    low_age = models.DecimalField(max_digits=10, decimal_places=2)
    high_age = models.DecimalField(max_digits=10, decimal_places=2)
    testes_no = models.IntegerField(default=0)
    testes_wgt = models.DecimalField(max_digits=10, decimal_places=2)
    t_e_no = models.IntegerField(default=0)
    t_e_wgt = models.DecimalField(max_digits=10, decimal_places=2)
    sem_ves_no = models.IntegerField(default=0)
    sem_ves_wgt = models.DecimalField(max_digits=10, decimal_places=2)
    pgl_no = models.IntegerField(default=0)
    pgl_wgt = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models
from patientapp.models import Patient
# Create your models here.

class Acting(models.Model):
    act = models.CharField(max_length=10)
    time = models.IntegerField()

    def __str__(self):
        return self.act

class ActingSet(models.Model):
    name = models.CharField(max_length=10)
    set = models.ManyToManyField(Acting)

    def __str__(self):
        return self.name

class Bed(models.Model):
    bed_num = models.CharField(max_length=5)
    bed_act = models.ForeignKey(ActingSet,blank=True,null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient,blank=True,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.bed_num
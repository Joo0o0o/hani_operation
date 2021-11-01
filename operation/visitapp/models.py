from django.db import models
from django.urls import reverse
from patientapp.models import Patient
# Create your models here.

class Symptoms(models.Model):
    name = models.CharField(max_length=10)

class Visit(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True,allow_unicode=True)
    symptom = models.ManyToManyField(Symptoms)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        index_together = [['id','slug']]

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

    def __str__(self):
        return self.name
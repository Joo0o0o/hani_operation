from django.db import models
from django.urls import reverse
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True,allow_unicode=True)
    phone_num = models.PositiveIntegerField()
    birthday = models.PositiveIntegerField()
    reg_num = models.PositiveIntegerField()
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at','-created_at']
        index_together = [['id','slug']]

    def get_absolute_url(self):
        return reverse('patientapp:product_detail', args=[self.id,self.slug])

    def __str__(self):
        return self.name
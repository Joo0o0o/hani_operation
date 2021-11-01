from django.contrib import admin
from patientapp.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Patient, PatientAdmin)

from django.forms import ModelForm

from patientapp.models import Patient


class PatientCreationForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','phone_num','birthday','reg_num','address','description']


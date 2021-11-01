from django.forms import ModelForm

from bedapp.models import Bed


class BedForm(ModelForm):
    class Meta:
        model = Bed
        fields = ['bed_act','patient']


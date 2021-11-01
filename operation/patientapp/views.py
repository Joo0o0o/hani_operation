from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView

from patientapp.models import Patient
from patientapp.forms import PatientCreationForm


class PatientCreateView(CreateView):
    model = Patient
    context_object_name = 'target_patient'
    form_class = PatientCreationForm
    template_name = 'patientapp/create.html'


    def get_success_url(self):
        return reverse('patientapp:detail', kwargs={'pk': self.object.pk})

    # def form_valid(self, form):
    #     temp_patient = form.save(commit=False)
    #     temp_patient.patient = self.request.patient
    #     temp_patient.save()
    #
    #     return super().form_valid(form)

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientCreationForm
    context_object_name = 'target_patient'
    template_name = 'patientapp/update.html'

    def get_success_url(self):
        return reverse('patientapp:detail', kwargs={'pk': self.object.pk})

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'target_patient'
    template_name = 'patientapp/detail.html'

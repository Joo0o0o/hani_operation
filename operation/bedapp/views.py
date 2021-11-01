from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DetailView
# Create your views here.
from .models import *
from .forms import BedForm


def BedView(request):
    beds = Bed.objects.all()

    return render(request,
                  'bedapp/bed.html',
                  {
                    'beds':beds,
                   }
                  )

class BedUpdateView(UpdateView):
    model = Bed
    form_class = BedForm
    context_object_name = 'target_bed'
    template_name = 'bedapp/update.html'

    def get_success_url(self):
        return reverse('patientapp:detail', kwargs={'pk': self.object.pk})

class PatientDetailView(DetailView):
    model = Bed
    context_object_name = 'target_bed'
    template_name = 'bedapp/detail.html'



from django.urls import path, include
from patientapp.views import PatientCreateView,PatientUpdateView, PatientDetailView

app_name = 'patientapp'

urlpatterns = [
    path( 'create/', PatientCreateView.as_view(), name='patient_create'),
    path( 'update/<int:pk>',PatientUpdateView.as_view(), name='update' ),
    path( 'detail/<int:pk>', PatientDetailView.as_view(), name='detail'),

]
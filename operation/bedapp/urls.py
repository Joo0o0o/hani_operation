
from django.urls import path, include
from .views import BedView

app_name = 'bedapp'

urlpatterns = [
    path('', BedView, name='bed'),
    path('update/<int:pk>', BedView, name='bed_update'),
]
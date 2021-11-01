from django.contrib import admin
from bedapp.models import Acting, ActingSet, Bed

class ActingAdmin(admin.ModelAdmin):
    list_display = ['id', 'act', 'time' ]

admin.site.register(Acting, ActingAdmin)

class ActingSetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(ActingSet, ActingSetAdmin)

class BedAdmin(admin.ModelAdmin):
    list_display = ['id', 'bed_num']
admin.site.register(Bed, BedAdmin)
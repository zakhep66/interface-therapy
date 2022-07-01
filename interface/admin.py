from django.contrib import admin
from .models import *


admin.site.register(Medication)
admin.site.register(MedOrder)
admin.site.register(LabEvent)
admin.site.register(LabType)
admin.site.register(Patient)
admin.site.register(PatientIcd)
admin.site.register(Therapy)
admin.site.register(Prescription)
admin.site.register(IndexType)
admin.site.register(User)
admin.site.register(MedIndex)
admin.site.register(OrderEntry)

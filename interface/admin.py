from django.contrib import admin
from django.contrib.auth.models import Group, User as DjangoUser

from .models import *


admin.site.unregister(Group)
admin.site.unregister(DjangoUser)

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

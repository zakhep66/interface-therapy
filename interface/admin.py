from django.contrib import admin
from django.contrib.auth.models import Group, User as DjangoUser

from .models import *
from .admin_filters import *


admin.site.unregister(Group)
admin.site.unregister(DjangoUser)

# admin.site.register(Medication)
# admin.site.register(MedOrder)
# admin.site.register(LabEvent)
# admin.site.register(LabType)
# admin.site.register(Patient)
# admin.site.register(PatientIcd)
# admin.site.register(Therapy)
# admin.site.register(Prescription)
# admin.site.register(IndexType)
# admin.site.register(User)
# admin.site.register(MedIndex)
# admin.site.register(OrderEntry)


admin.site.register(Medication)
admin.site.register(Medorder)
admin.site.register(Labevent)
admin.site.register(Labtype)
admin.site.register(Patient)
admin.site.register(PatientIcd)
admin.site.register(Therapy)
admin.site.register(Prescription)
# admin.site.register(Indextype)
# admin.site.register(Customer)
admin.site.register(Medindex)
admin.site.register(OrderEntry)

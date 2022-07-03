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


admin.site.register(Medication, MedicationFilters)
admin.site.register(Medorder, MedOrderFilters)
admin.site.register(Labevent, LabEventFilters)
admin.site.register(Labtype, LabTypeFilters)
admin.site.register(Patient, PatientFilters)
admin.site.register(PatientIcd, PatientIcdFilters)
admin.site.register(Therapy, TherapyFilters)
admin.site.register(Prescription, PrescriptionFilters)
# admin.site.register(Indextype)
# admin.site.register(Customer)
admin.site.register(Medindex, MedIndexFilters)
admin.site.register(OrderEntry,  OrderEntryFilters)

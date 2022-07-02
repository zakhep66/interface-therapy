from django.contrib import admin
from django.contrib.auth.models import Group, User as DjangoUser

from .models import *
from .admin_filters import *


admin.site.unregister(Group)
admin.site.unregister(DjangoUser)

admin.site.register(Medication, MedicationFilters)
admin.site.register(MedOrder, MedOrderFilters)
admin.site.register(LabEvent, LabEventFilters)
admin.site.register(LabType, LabTypeFilters)
admin.site.register(Patient, PatientFilters)
admin.site.register(PatientIcd, PatientIcdFilters)
admin.site.register(Therapy, TherapyFilters)
admin.site.register(Prescription, PrescriptionFilters)
admin.site.register(IndexType, IndexTypeFilters)
admin.site.register(User, UserFilters)
admin.site.register(MedIndex, MedIndexFilters)
admin.site.register(OrderEntry, OrderEntryFilters)

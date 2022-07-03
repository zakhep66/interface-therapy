from django.contrib import admin


class LabTypeFilters(admin.ModelAdmin):
	list_display = [
		'name', "mu", 'lolim', 'uplim'
	]
	list_filter = [
		'mu', 'created', 'changed'
	]

	search_fields = [
		'name'
	]


class LabEventFilters(admin.ModelAdmin):
	list_display = ['patient_id', 'value', 'aflag', 'taken']
	list_filter = ['labtype', 'taken']
	search_fields = ['id', 'patient_id', 'labtype']


class IndexTypeFilters(admin.ModelAdmin):
	list_display = ['name', 'lolimnum', 'uplimnum']
	list_filter = ['created', 'changed']
	search_fields = ['name']


class PatientIcdFilters(admin.ModelAdmin):
	list_display = ['code', 'patient']
	list_filter = ['created', 'changed']
	search_fields = ['code']


class MedOrderFilters(admin.ModelAdmin):
	list_display = ['supplier', 'status', 'form_date', 'delivery_date']
	list_filter = ['supplier', 'status', 'created', 'changed']
	search_fields = ['supplier', 'status']


class OrderEntryFilters(admin.ModelAdmin):
	list_display = ['medication_id', 'medorder', 'amount']
	list_filter = ['medication_id__nomenclature', 'medorder__supplier', 'created', 'changed']
	search_fields = ['medication_id__nomenclature', 'medorder__supplier']


class TherapyFilters(admin.ModelAdmin):
	list_display = ['patient_id', 'date', 'time_period', 'status']
	list_filter = ['status', 'date', 'created', 'changed']
	search_fields = ['patient_id__full_name']


class MedIndexFilters(admin.ModelAdmin):
	list_display = ['value', 'aflag', 'therapy_id', 'index_type']
	list_filter = ['value']
	search_fields = ['value', 'aflag']


class PrescriptionFilters(admin.ModelAdmin):
	list_display = ['administration_type', 'medication_id', 'dose_amount', 'therapy_id']
	list_filter = ['medication_id__nomenclature', 'administration_type', 'created', 'changed']
	search_fields = ['medication_id__nomenclature']


class PatientFilters(admin.ModelAdmin):
	list_display = ['full_name', 'ambulatory_card', 'phone_number', 'email', 'date_of_birth', 'sex']
	list_filter = ['sex', 'date_of_birth', 'created', 'changed']
	search_fields = ['full_name', 'ambulatory_card', 'phone_number', 'email', 'contact_person']


class MedicationFilters(admin.ModelAdmin):
	list_display = ['nomenclature', 'manufacturer', 'dose_form', 'dose_val', 'mu']
	list_filter = ['manufacturer', 'mu', 'created', 'changed']
	search_fields = ['nomenclature', 'mu']


class UserFilters(admin.ModelAdmin):
	list_display = ['login', 'roles']
	list_filter = ['roles']
	search_fields = ['login']

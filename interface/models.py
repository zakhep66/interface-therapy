# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    login = models.CharField(unique=True, max_length=127)
    password = models.CharField(max_length=127)
    roles = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Labevent(models.Model):
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    labtype = models.ForeignKey('Labtype', models.DO_NOTHING)
    value = models.CharField(max_length=200, blank=True, null=True)
    valuenum = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    taken = models.DateTimeField()
    aflag = models.CharField(max_length=32, blank=True, null=True)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'labevent'


class Labtype(models.Model):
    name = models.CharField(max_length=100)
    specimen = models.CharField(max_length=100)
    mu = models.CharField(max_length=32, blank=True, null=True)
    lolim = models.CharField(max_length=200, blank=True, null=True)
    lolimnum = models.FloatField(blank=True, null=True)
    uplim = models.CharField(max_length=200, blank=True, null=True)
    uplimnum = models.FloatField(blank=True, null=True)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'labtype'
        unique_together = (('name', 'specimen', 'mu'),)


class Medication(models.Model):
    nomenclature = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120, blank=True, null=True)
    dose_form = models.CharField(max_length=50)
    dose_val = models.FloatField()
    mu = models.CharField(max_length=32)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medication'


class Medindex(models.Model):
    therapy = models.ForeignKey('Therapy', models.DO_NOTHING)
    index_type = models.SmallIntegerField()
    value = models.FloatField(blank=True, null=True)
    aflag = models.CharField(max_length=32, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medindex'


class Medorder(models.Model):
    supplier = models.CharField(max_length=120)
    form_date = models.DateTimeField()
    delivery_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medorder'


class OrderEntry(models.Model):
    medication = models.ForeignKey(Medication, models.DO_NOTHING)
    medorder = models.ForeignKey(Medorder, models.DO_NOTHING)
    amount = models.IntegerField()
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_entry'


class Patient(models.Model):
    full_name = models.CharField(max_length=96)
    phone_number = models.CharField(max_length=11)
    adverse_reactions = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    sex = models.SmallIntegerField()
    created = models.DateTimeField()
    changed = models.DateTimeField()
    email = models.CharField(max_length=120, blank=True, null=True)
    contact_person = models.CharField(max_length=11, blank=True, null=True)
    ambulatory_card = models.CharField(unique=True, max_length=10, blank=True, null=True)
    finance_source = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class PatientIcd(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    code = models.CharField(max_length=8)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'patient_icd'
        unique_together = (('patient', 'code'),)


class Prescription(models.Model):
    therapy = models.OneToOneField('Therapy', models.DO_NOTHING)
    medication = models.ForeignKey(Medication, models.DO_NOTHING)
    dose_amount = models.IntegerField()
    substance_amount = models.FloatField()
    administration_type = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prescription'


class Therapy(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    date = models.DateField()
    time_period = models.SmallIntegerField()
    status = models.SmallIntegerField()
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'therapy'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


createdAt = "Время создания записи"
changedAt = "Время изменения записи"


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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(f'Логин: {self.login}, роль: {self.roles}')


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
        verbose_name = "Анализ"
        verbose_name_plural = "Анализы"

    def __str__(self):
        return str(self.value)


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
        verbose_name = "Вид анализа"
        verbose_name_plural = "Виды анализа"

    def __str__(self):
        return str(self.name)


class Medication(models.Model):
    nomenclature = models.CharField(max_length=120, verbose_name="Номенклатура препарата")
    manufacturer = models.CharField(max_length=120, blank=True, null=True, verbose_name="Производитель препарата")
    dose_form = models.CharField(max_length=50, verbose_name="Описание единицы учёта препарата")
    dose_val = models.FloatField(verbose_name="Кол-во вещества в единице учёта")
    mu = models.CharField(max_length=32, verbose_name="Единицы измерения вещества лекарства")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'medication'
        verbose_name = "Препараты"
        verbose_name_plural = "Препарат"

    def __str__(self):
        return str(self.nomenclature)


class Medindex(models.Model):
    therapy = models.ForeignKey('Therapy', models.DO_NOTHING, verbose_name="Номер терапии")
    index_type = models.SmallIntegerField(verbose_name="Тип индекса")
    value = models.FloatField(blank=True, null=True, verbose_name="Значение индекса")
    aflag = models.CharField(max_length=32, blank=True, null=True, verbose_name="Отклонение от нормы")
    comments = models.TextField(blank=True, null=True, verbose_name="Примечание специалиста")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'medindex'
        verbose_name = "Клинический индекс"
        verbose_name_plural = "Клинические индексы"

    def __str__(self):
        return str(self.value)


class Medorder(models.Model):
    supplier = models.CharField(max_length=120, verbose_name="Поставщик препаратов")
    form_date = models.DateTimeField(verbose_name="Время формирования и отправки заказа")
    delivery_date = models.DateTimeField(blank=True, null=True, verbose_name="Время поступления заказа")
    status = models.SmallIntegerField(verbose_name="Статус заказа")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'medorder'
        verbose_name = "Заказ в аптеку"
        verbose_name_plural = "Заказы в аптеку"

    def __str__(self):
        return str(self.supplier)


class OrderEntry(models.Model):
    medication = models.ForeignKey(Medication, models.DO_NOTHING, verbose_name="Номер препарат")
    medorder = models.ForeignKey(Medorder, models.DO_NOTHING, verbose_name="Номер заказа в аптеке")
    amount = models.IntegerField(verbose_name="Кол-во единиц на заказ")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'order_entry'
        verbose_name = "Запись заказа"
        verbose_name_plural = "Записи заказов"

    def __str__(self):
        return str(f'Препарат: {self.medication.nomenclature}')


sex_choices = (
    (1, 'Мужской'),
    (2, 'Женский')
)

class Patient(models.Model):
    full_name = models.CharField(max_length=96, verbose_name="ФИО пациента")
    phone_number = models.CharField(max_length=11, verbose_name="Номер телефона пациента")
    adverse_reactions = models.TextField(blank=True, null=True, verbose_name="Нежелательные реакции")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    sex = models.SmallIntegerField(verbose_name="Пол пациента", choices=sex_choices)
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)
    email = models.CharField(max_length=120, blank=True, null=True, verbose_name="Электронная почта")
    contact_person = models.CharField(max_length=11, blank=True, null=True, verbose_name="Телефонный номер контактного лица")
    ambulatory_card = models.CharField(unique=True, max_length=10, blank=True, null=True, verbose_name="Номер амбулаторной карты из системы Interin")
    finance_source = models.SmallIntegerField(blank=True, null=True, verbose_name="Источник финансирования")

    class Meta:
        managed = False
        db_table = 'patient'
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return str(self.full_name)


class PatientIcd(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, verbose_name="Пациент")
    code = models.CharField(max_length=8, verbose_name="Строковый код диагноза по классификации МКБ")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'patient_icd'
        unique_together = (('patient', 'code'),)
        verbose_name = "Диагноз МКБ"
        verbose_name_plural = "Диагнозы МКБ"

    def __str__(self):
        return str(self.code)


class Prescription(models.Model):
    therapy = models.ForeignKey('Therapy', models.DO_NOTHING, verbose_name="Номер терапии")
    medication = models.ForeignKey(Medication, models.DO_NOTHING, verbose_name="Препарат")
    dose_amount = models.IntegerField(verbose_name="Кол-во списанного к терапии лекарства в дозах")
    substance_amount = models.FloatField(verbose_name="Кол-во списанного к терапии вещества лекарства")
    administration_type = models.SmallIntegerField(blank=True, null=True, verbose_name="Тип введения препарата")
    comments = models.TextField(blank=True, null=True, verbose_name="Примечание к назначению")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'prescription'
        verbose_name = "Лекарственное назначение"
        verbose_name_plural = "Лекарственные назначения"

    def __str__(self):
        return str(self.administration_type)


class Therapy(models.Model):
    patient = models.ForeignKey(Patient, models.DO_NOTHING, verbose_name="Пациент")
    date = models.DateField(verbose_name="Дата проведения терапии")
    time_period = models.SmallIntegerField(verbose_name="Время проведения терапии")
    status = models.SmallIntegerField(verbose_name="Статус терапии")
    comments = models.TextField(blank=True, null=True, verbose_name="Примечание к записи о терапии")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

    class Meta:
        managed = False
        db_table = 'therapy'
        verbose_name = "Запись о терапии"
        verbose_name_plural = "Записи о терапии"

    def __str__(self):
        return str(f'Пациент: {self.patient.full_name}, дата: {self.date}')

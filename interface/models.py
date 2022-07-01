from django.db import models

createdAt = "Время создания записи"
changedAt = "Время изменения записи"


class Medication(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True)
    name = models.CharField(max_length=120, verbose_name="Официальное название препарата")
    nomenclature = models.CharField(max_length=120, verbose_name="Номенклатура препарата")
    manufacturer = models.CharField(max_length=120, verbose_name="Производитель препарата")
    dose_form = models.CharField(max_length=50, verbose_name="Описание единицы учёта препарата")
    dose_val = models.FloatField(verbose_name="Кол-во вещества в единице учёта")
    mu = models.CharField(max_length=32, verbose_name="Единицы измерения вещества лекарства")
    amount = models.IntegerField(verbose_name="Кол-во препарата в единицах учёта (мелких единицах)")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class MedOrder(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True)
    supplier = models.CharField(max_length=120, verbose_name="Поставщик препаратов")
    form_date = models.DateTimeField(verbose_name="Время формирования и отправки заказа")
    delivery_rate = models.DateTimeField(verbose_name="Время поступления заказа")
    status = models.SmallIntegerField(verbose_name="Статус заказа")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class LabEvent(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True)
    lab_type = models.ForeignKey("LabType", on_delete=models.DO_NOTHING, verbose_name="ID вида анализа (внешний ключ)")
    patient_id = models.ForeignKey("Patient", on_delete=models.CASCADE)
    value = models.CharField(max_length=200, verbose_name="Показатель")
    valuenum = models.FloatField(verbose_name="Числовой показатель")
    comments = models.TextField(verbose_name="Комментарий специалиста")
    taken = models.DateTimeField(verbose_name="Время взятия анализа")
    aflag = models.CharField(max_length=32, verbose_name="Отклонение от нормы")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class LabType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название анализа")
    mu = models.CharField(max_length=32, verbose_name="Единицы измерения")
    lolim = models.CharField(max_length=200, verbose_name="Нижняя граница нормы показателя")
    lolimnum = models.FloatField(verbose_name="Числовая нижняя граница нормы показателя")
    uplim = models.CharField(max_length=200, verbose_name="Верхняя граница нормы показателя")
    uplimnum = models.FloatField(verbose_name="Числовая верхняя граница нормы показателя")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class Patient(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True)
    full_name = models.CharField(max_length=96, verbose_name="ФИО пациента")
    phone_number = models.CharField(max_length=11, verbose_name="Номер телефона пациента")
    adverse_reactions = models.TextField(verbose_name="Нежелательные реакции")
    date_of_birth = models.DateTimeField(verbose_name="Дата рождения")
    sex = models.SmallIntegerField(verbose_name="Пол пациента (формат ISO/IEC 5218)")
    email = models.CharField(max_length=120, verbose_name="Электронная почта")
    contact_person = models.CharField(max_length=11, verbose_name="Телефонный номер контактного лица")
    ambulatory_card = models.CharField(max_length=10, verbose_name="Номер амбулаторной карты из системы Interin")
    finance_source = models.SmallIntegerField(verbose_name="Источник финансирования")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class PatientIcd(models.Model):
    patient_id = models.ForeignKey("Patient", on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=8, verbose_name="Строковый код диагноза по классификации МКБ")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class Therapy(models.Model):
    patient_id = models.ForeignKey("Patient", on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(verbose_name="Время начала терапии")
    end_time = models.DateTimeField(verbose_name="Время окончания терапии")
    cabinet = models.CharField(max_length=15, verbose_name="Кабинет, где будет проходить терапия")
    status = models.SmallIntegerField(verbose_name="Статус терапии")
    comments = models.TextField(verbose_name="Примечание к записи о терапии")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class Prescription(models.Model):
    id = models.UUIDField(verbose_name="UUID", primary_key=True)
    therapy_id = models.ForeignKey("Therapy", on_delete=models.DO_NOTHING)
    medication_id = models.ForeignKey("Medication", on_delete=models.DO_NOTHING)
    dose_amount = models.IntegerField(verbose_name="Кол-во списанного к терапии лекарства в дозах")
    substance_amount = models.FloatField(verbose_name="Кол-во списанного к терапии вещества лекарства")
    administration_type = models.SmallIntegerField(verbose_name="Тип введения препарата")
    comments = models.TextField(verbose_name="Примечание к назначению")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class IndexType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название индекса")
    lolimnum = models.FloatField(verbose_name="Числовая нижняя граница нормы показателя")
    uplimnum = models.FloatField(verbose_name="Числовая верхняя граница нормы показателя")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)


class User(models.Model):
    id = models.UUIDField(verbose_name="UUID пользователя (первичный ключ)", primary_key=True)
    login = models.CharField(max_length=127, verbose_name="Логин пользователя")
    password = models.CharField(max_length=127, verbose_name="Пароль для входа (ключ шифрования BCrypt)")
    roles = models.IntegerField(verbose_name="Роли пользователя")


class MedIndex(models.Model):
    id = models.UUIDField(verbose_name="ID терапии (внешний ключ)", primary_key=True)
    therapy_id = models.ForeignKey("Therapy", verbose_name="ID терапии (внешний ключ)", on_delete=models.DO_NOTHING)
    index_type_id = models.ForeignKey("IndexType", verbose_name="Вид индекса", on_delete=models.DO_NOTHING)
    value = models.FloatField(verbose_name="Значение индекса")
    aflag = models.CharField(max_length=32, verbose_name="Отклонение от нормы")
    comments = models.TextField(verbose_name="Примечание специалиста")
    created = models.TimeField(verbose_name=createdAt)
    changed = models.TimeField(verbose_name=changedAt)


class OrderEntry(models.Model):
    medication_id = models.ForeignKey("Medication", on_delete=models.DO_NOTHING,
                                      verbose_name="UUID препарата (внешний ключ)")
    medorder = models.ForeignKey("MedOrder", on_delete=models.DO_NOTHING,
                                 verbose_name="UUID заказа в аптеку (внешний ключ)")
    amount = models.IntegerField(verbose_name="Кол-во единиц на заказ")
    created = models.DateTimeField(verbose_name=createdAt)
    changed = models.DateTimeField(verbose_name=changedAt)

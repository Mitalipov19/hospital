from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'doctor'),
        ('patient', 'patient')
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    phone_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='profile_images/')
    adress = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Patient(UserProfile):
    emergency_contact = models.CharField(max_length=16, blank=True, null=True)
    blood_type = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Doctor(UserProfile):
    SPECIALTIES_CHOICES = (
        ("Терапевт", "Терапевт"),
        ("Хирург", "Хирург"),
        ("Педиатр", "Педиатр"),
        ("Гинеколог", "Гинеколог"),
        ("Кардиолог", "Кардиолог"),
        ("Невролог", "Невролог"),
        ("Офтальмолог", "Офтальмолог"),
        ("Дерматолог", "Дерматолог"),
        ("Стоматолог", "Стоматолог"),
        ("Эндокринолог", "Эндокринолог"),
        ("Психиатр", "Психиатр"),
        ("Реаниматолог", "Реаниматолог"),
        ("Уролог", "Уролог"),
        ("Аллерголог", "Аллерголог"),
        ("Инфекционист", "Инфекционист"),
        ("Лор (оториноларинголог)", "Лор (оториноларинголог)"),
        ("Физиотерапевт", "Физиотерапевт"),
        ("Рентгенолог", "Рентгенолог"),
        ("Токсиколог", "Токсиколог"),
        ("Химиотерапевт", "Химиотерапевт")
    )
    specialty = models.CharField(max_length=32, choices=SPECIALTIES_CHOICES)
    department = models.CharField(max_length=150)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    qualifications = models.CharField(max_length=32)
    experience_year = models.PositiveSmallIntegerField(default=0)
    WORKING_DAYS = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    working_days_choices = MultiSelectField(choices=WORKING_DAYS)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Appointments(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointment_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_doctor')
    datetime = models.DateTimeField()
    STATUS_CHOICES = (
        ('schedule', 'schedule'),
        ('failed', 'failed'),
        ('Completed', 'Completed')
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    price = models.PositiveSmallIntegerField(default=0)
    notes = models.TextField()

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.datetime}'


class MedicalRecord(models.Model): #
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='rec_patient')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='rec_doctor')
    diagnosis = models.TextField() #диагноз.
    treatment = models.TextField() #лечение.
    prescribed_medication  = models.TextField() #назначенные лекарства.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient} - {self.doctor} - {self.diagnosis}'


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reviews')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.doctor} - {self.patient}'



class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    created_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='chat_image/', null=True, blank=True)
    video = models.FileField(upload_to='chat_video/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name']


class PatientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name']


class DoctorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']


class AppointmentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['patient', 'doctor', 'datetime']


class AppointmentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ['patient', 'doctor', 'datetime', 'status', 'price', 'notes']


class MedicalRecordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis']


class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    doctor = DoctorSimpleSerializer()
    patient = PatientSimpleSerializer()
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class FeedbackSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    doctor = DoctorSimpleSerializer()
    patient = PatientSimpleSerializer()
    class Meta:
        model = Feedback
        fields = ['doctor', 'patient', 'rating', 'comment', 'created_at']


class PatientSerializer(serializers.ModelSerializer):
    appointment_patient = AppointmentsDetailSerializer(many=True, read_only=True)
    rec_patient = MedicalRecordDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Patient
        fields = ['emergency_contact', 'blood_type', 'id', 'first_name', 'last_name',
                  'appointment_patient', 'rec_patient']


class DoctorSerializer(serializers.ModelSerializer):
    reviews = FeedbackSerializer(many=True, read_only=True)
    appointment_doctor = AppointmentsDetailSerializer(many=True, read_only=True)
    rec_doctor = MedicalRecordDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'specialty', 'shift_start', 'shift_end',
                  'qualifications', 'experience_year', 'working_days_choices', 'reviews',
                  'appointment_doctor', 'rec_doctor']
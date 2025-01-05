from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['specialty', 'department', 'working_days_choices']
    permission_classes = [CheckSelf]


class AppointmentsListViewSet(generics.ListAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsListSerializer
    permission_classes = [CheckPatient]


class AppointmentsDetailViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsDetailSerializer
    permission_classes = [CheckPatient]

class MedicalRecordListViewSet(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializer


class MedicalRecordDetailViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordDetailSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [CheckPatient]
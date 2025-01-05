from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
router=routers.DefaultRouter()

router.register(r'users', UserProfileViewSet, basename='users_list')
router.register(r'patient', PatientViewSet, basename='patient_list')
router.register(r'doctor', DoctorViewSet, basename='doctor_list')
router.register(r'appointment-detail', AppointmentsDetailViewSet, basename='appointment_detail')
router.register(r'records-detail', MedicalRecordDetailViewSet, basename='records_detail')
router.register(r'feedback', FeedbackViewSet, basename='feedback_list')


urlpatterns=[
    path('', include(router.urls)),
    path('appointment_list', AppointmentsListSerializer),
    path('records_list', MedicalRecordListSerializer)
]
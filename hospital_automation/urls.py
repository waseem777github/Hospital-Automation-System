from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('doctors', views.doctors, name='doctors'),
    path('api/receive_incoming_patient',
         views.receive_patient, name='incoming_patient'),
    path('reception', views.reception, name="reception"),
    path('reception/ajax/<int:id>', views.autocomplete, name="autocomplete"),
    path('doctor/<int:patient_id>', views.prescriptions, name="prescriptions"),
    path('reception/ajax/load-doctors',
         views.load_doctors, name='ajax_load_doctors'),
    path('dispensary', views.patient_to_dispensary, name="dispensary"),
    path('api/receive_incoming_patient_to_dispensary',
         views.receive_incoming_patient_to_dispensary, name="incoming_patient_to_dispensary"),
    path('dispensary/<int:patient_id>',
         views.medication_of_patient, name="medication"),
    path('dispensary/<int:patient_id>/is_done',
         views.is_done_with_patient, name="is_done"),
    path('test', views.test, name="test"),
    path('api/receive_incoming_patient_for_test',
         views.receive_incoming_patient_for_test, name="incoming_patient_for_test"),
    path('test/<int:patient_id>', views.patient_to_test, name="patient_to_test"),
    path('test/<int:patient_id>/patient_is_done_with_test',
         views.patient_is_done_with_test, name="is_done_with_test"),
    path('doctor/<int:patient_id>/send_prescriptions',
         views.send_prescriptions, name="send_prescriptions"),
    path('doctor_details', views.doctor_details, name="doctor_details"),
    path('helpers', views.helpers, name="helpers"),
    path('patient_records/', views.patient_records, name='patient_records'),
    path('patient_records/<int:patient_id>/',
         views.patient_detail, name='patient_detail'),
    path('statistics', views.statistics, name="statistics"),

    path('patient_prescriptions/ajax/<int:id>', views.autocomplete_medicine, name="autocomplete_medicine"),
]

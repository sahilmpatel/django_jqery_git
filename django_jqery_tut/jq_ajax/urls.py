from django.urls import path
from .views import signup_view,validate_details

app_name = 'jq_ajax'

urlpatterns = [
    path('signup_view',signup_view,name='signup_view'),
    path('ajax/validate_details',validate_details,name='validate_details'),
]
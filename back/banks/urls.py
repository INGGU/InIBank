from django.urls import path
from . import views


app_name = 'banks'
urlpatterns = [
    path('save-time-deposits/', views.save_time_deposits, name='save_time_deposits'),
]

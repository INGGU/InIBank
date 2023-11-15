from django.urls import path
from . import views


app_name = 'banks'
urlpatterns = [
    path('save-time-deposits/', views.save_time_deposits, name='save_time_deposits'),
    path('save-savings/', views.save_savings, name='save_savings'),
    path('save-mortgage-loans/', views.save_mortgage_loans, name='save_mortgage_loans'),
    # path('save-jeonse-loans/', views.jeonse_loans, name='jeonse_loans'),
    # path('save-personal-loans/', views.personal_loans, name='personal_loans'),
]

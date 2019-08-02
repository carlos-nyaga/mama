from django.urls import path
from django.views.generic import TemplateView
from .apps import DashboardConfig
from . import views
from django.contrib.auth.views import LoginView as LV, LogoutView


app_name = DashboardConfig.name

urlpatterns = [

    # path('', views.home, name='home'),
    path('', views.index, name='index'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('accounts/login/', LV.as_view(template_name = 'dashboard/login_2.html'), name="login"),

    path('attendees/', views.attendee_list, name='attendees'),
    path('attendees/create/', views.attendee_create, name='attendee-create'),
    path('attendees/update/<uuid:pk>/', views.attendee_update, name='attendee-update'),
    path('attendees/delete/<uuid:pk>/', views.attendee_delete, name='attendee-delete'),

]


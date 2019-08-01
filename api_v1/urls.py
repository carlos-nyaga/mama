from django.urls import path
from .apps import ApiV1Config
from . import views

app_name = ApiV1Config.name

urlpatterns = [
    path('v1/attendees/<uuid:pk>/', 
    views.get_delete_update_attendee, 
    name='get_delete_update_attendee'),

    path('v1/attendees/', 
    views.get_post_attendees, 
    name='get_post_attendees')


]
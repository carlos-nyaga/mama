from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from api_v1.models import Attendee

@admin.register(Attendee)
class AttendeeAdmin(ImportExportModelAdmin):
    pass

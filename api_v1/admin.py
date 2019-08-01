from django.contrib import admin
from .models import Attendee
# Register your models here.
MAX_SHOW_ALL = 10000
PER_PAGE = 500

# @admin.register(Attendee)
# class AttendeeAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'updated_at', 'created_at')
#     search_fields = ['first_name', 'last_name']
#     date_hierarchy = 'created_at'
#     list_max_show_all = MAX_SHOW_ALL
#     list_per_page = PER_PAGE

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)


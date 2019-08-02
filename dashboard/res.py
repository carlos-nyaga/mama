from import_export import resources

from api_v1.models import Attendee


class AttendeeResource(resources.ModelResource):
    class Meta:
        model = Attendee
from django.test import TestCase
from ..models import Attendee

class AttendeeTest(TestCase):
    """ Test Model Attendee """

    def setUp(self):
        Attendee.objects.create(
            first_name='John', middle_name='Doolittle', last_name='Doe',
            phone_number='373(343)422', email='john@doe.com')
        Attendee.objects.create(
            first_name='Jane', middle_name='', last_name='Doe',
            phone_number='373(344)452', email='jane@doe.com')
    
    def test_full_name(self):
        attendee_john = Attendee.objects.get(first_name='John')
        attendee_jane = Attendee.objects.get(first_name='Jane')

        self.assertEqual(attendee_john.__str__(), "John Doolittle Doe")
        self.assertEqual(attendee_jane.__str__(), "Jane  Doe")

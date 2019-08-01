import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Attendee
from ..serializers import AttendeeSerializer
import uuid
# initialize the APIClient app
client = Client()
# client.credentials(HTTP_AUTHORIZATION='Token 658e37494183e25173ff5da89669f9d6de9d1aba')
header = {'HTTP_AUTHORIZATION': 'Token 658e37494183e25173ff5da89669f9d6de9d1aba'}
class GetAllAttendeesTest(TestCase):
    """ Test module for GET all attendees API """

    def setUp(self):
        Attendee.objects.create(
            first_name='John', middle_name='Doolittle', last_name='Doe',
            phone_number='373(343)422', email='john@doe.com')
        Attendee.objects.create(
            first_name='Jane', middle_name='', last_name='Doe',
            phone_number='373(344)452', email='jane@doe.com')
        Attendee.objects.create(
            first_name='Pablo', middle_name='Elduerdo', last_name='Escobar',
            phone_number='356(356)472', email='pablo@escobar.com')
        Attendee.objects.create(
            first_name='Elle', middle_name='', last_name='Mez',
            phone_number='353(334)322', email='elle@mez.com')

    def test_get_all_attendees(self):
        # get API response
        response = client.get(reverse('api_v1:get_post_attendees'), {}, **header)

        # get data from db
        attendees = Attendee.objects.all()
        serializer = AttendeeSerializer(attendees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleAttendeeTest(TestCase):
    """ Test module for GET single attendee API """

    def setUp(self):
        self.john = Attendee.objects.create(
            first_name='John', middle_name='Doolittle', last_name='Doe',
            phone_number='373(343)422', email='john@doe.com')
        self.jane = Attendee.objects.create(
            first_name='Jane', middle_name='', last_name='Doe',
            phone_number='373(344)452', email='jane@doe.com')
        self.pablo = Attendee.objects.create(
            first_name='Pablo', middle_name='Elduerdo', last_name='Escobar',
            phone_number='356(356)472', email='pablo@escobar.com')
        self.elle = Attendee.objects.create(
            first_name='Elle', middle_name='', last_name='Mez',
            phone_number='353(334)322', email='elle@mez.com')

    def test_get_valid_single_attendee(self):
        response = client.get(
            reverse('api_v1:get_delete_update_attendee', kwargs={'pk': self.pablo.pk}), {}, **header)
        attendee = Attendee.objects.get(pk=self.pablo.pk)
        serializer = AttendeeSerializer(attendee)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_attendee(self):
        response = client.get(
            reverse('api_v1:get_delete_update_attendee', kwargs={'pk': uuid.uuid4()}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewAttendeeTest(TestCase):
    """ Test module for inserting a new attendee """

    def setUp(self):
        self.valid_payload = {
            'first_name': 'John',
            'middle_name': 'Doolitle',
            'last_name': 'Doe',
            'phone_number': '224(242)2422',
            'email': 'john@doolittle.com'
        }
        self.invalid_payload = {
            'first_name': '',
            'middle_name': 'Doolitle',
            'last_name': '',
            'phone_number': '224(242)2422',
            'email': 'john@doolittle.com'
        }

    def test_create_valid_attemdee(self):
        response = client.post(
            reverse('api_v1:get_post_attendees'),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_attendee(self):
        response = client.post(
            reverse('api_v1:get_post_attendees'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json', **header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleAttendeeTest(TestCase):
    """ Test module for updating an existing attendee record """

    def setUp(self):
        self.john = Attendee.objects.create(
            first_name='John', middle_name='Doolittle', last_name='Doe',
            phone_number='373(343)422', email='john@doe.com')
        self.jane = Attendee.objects.create(
            first_name='Jane', middle_name='', last_name='Doe',
            phone_number='373(344)452', email='jane@doe.com')
        self.valid_payload = {
            'first_name': 'John',
            'middle_name': 'Doolitle',
            'last_name': 'Doe',
            'phone_number': '224(242)2422',
            'email': 'john@doolittle.com'
        }
        self.invalid_payload = {
            'first_name': '',
            'middle_name': 'Doolitle',
            'last_name': '',
            'phone_number': '224(242)2422',
            'email': ''
        }

    def test_valid_update_attendee(self):
        response = client.put(
            reverse('api_v1:get_delete_update_attendee', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json', **header
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_attendee(self):
        response = client.put(
            reverse('api_v1:get_delete_update_attendee', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json', **header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleAttendeeTest(TestCase):
    """ Test module for deleting an existing attendee record """

    def setUp(self):
        self.john = Attendee.objects.create(
            first_name='John', middle_name='Doolittle', last_name='Doe',
            phone_number='373(343)422', email='john@doe.com')
        self.jane = Attendee.objects.create(
            first_name='Jane', middle_name='', last_name='Doe',
            phone_number='373(344)452', email='jane@doe.com')

    def test_valid_delete_attendee(self):
        response = client.delete(
            reverse('api_v1:get_delete_update_attendee', 
            kwargs={'pk': self.john.pk}), **header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_attendee(self):
        response = client.delete(
            reverse('api_v1:get_delete_update_attendee', 
            kwargs={'pk': uuid.uuid4()}), **header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Attendee
from .serializers import AttendeeSerializer
import uuid

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_attendee(request, pk):
    permission_classes = (IsAuthenticated,)             # <-- And here
    try:
        attendee = Attendee.objects.get(pk=pk)
    except Attendee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single attendee
    if request.method == 'GET':
        serializer = AttendeeSerializer(attendee)
        return Response(serializer.data)
    
    # update details of a single attendee
    if request.method == 'PUT':
        serializer = AttendeeSerializer(attendee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single attendee
    if request.method == 'DELETE':
        attendee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def get_post_attendees(request):
    permission_classes = (IsAuthenticated,)             # <-- And here
    # get all attendees
    if request.method == 'GET':
        attendees = Attendee.objects.all()
        serializer = AttendeeSerializer(attendees, many=True)
        return Response(serializer.data)
    # insert a new record for an attendee
    elif request.method == 'POST':
        data = {
            'first_name': request.data.get('first_name'),
            'middle_name': request.data.get('middle_name'),
            'last_name': request.data.get('last_name'),
            'phone_number': request.data.get('phone_number'),
            'email': request.data.get('email'),
            'token': uuid.uuid4()
        }

        serializer = AttendeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

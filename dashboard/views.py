from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api_v1.models import Attendee
from rest_framework.authtoken.models import Token


def home(request):
    return render(request, "dashboard/landing.html", context={})

def index(request):
    return redirect(reverse("dashboard:dashboard"))


@login_required
def dashboard(request):
    return render(request, "dashboard/index.html", context={})

@login_required
def attendee_list(request):
	attendees = Attendee.objects.all()
	context = {
		'attendees': attendees,
		'authToken': Token.objects.get_or_create(user=request.user)[0]}
	return render(request, "dashboard/attendee_list.html", context)

from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from api_v1.models import Attendee
from rest_framework.authtoken.models import Token
from .forms import AttendeeForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .res import AttendeeResource
def home(request):
    return render(request, "dashboard/landing.html", context={})

def index(request):
    return redirect(reverse("dashboard:dashboard"))


@login_required
def dashboard(request):
    return render(request, "dashboard/index.html", context={"attendees":Attendee.objects.all().count()})


@login_required
def attendee_list(request):
    attendees = Attendee.objects.all()
    context = {
        'attendees': attendees,
        'authToken': Token.objects.get_or_create(user=request.user)[0]}
    return render(request, "dashboard/attendee_list.html", context)
@login_required
def save_all(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            attendees = Attendee.objects.all()
            data['attendee_list'] = render_to_string('dashboard/attendee_list_content.html',{'attendees':attendees})
        else:
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required
def attendee_create(request):
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
    else:
        form = AttendeeForm()
    return save_all(request,form,'dashboard/attendee_create.html')


@login_required
def attendee_update(request, pk):
    attendee = get_object_or_404(Attendee,pk=pk)
    if request.method == 'POST':
        form = AttendeeForm(request.POST,instance=attendee)
    else:
        form = AttendeeForm(instance=attendee)
    return save_all(request,form,'dashboard/attendee_update.html')


@login_required
def attendee_delete(request, pk):
    print("weeeeeee {}".format(pk))
    data = dict()
    attendee = get_object_or_404(Attendee,pk=pk)
    if request.method == "POST":
        attendee.delete()
        data['form_is_valid'] = True
        attendees = Attendee.objects.all()
        data['attendee_list'] = render_to_string('dashboard/attendee_list_content.html',{'attendees':attendees})
    else:
        context = {'attendee':attendee}
        data['html_form'] = render_to_string('dashboard/attendee_delete.html',context,request=request)

    return JsonResponse(data)


@login_required
def attendees_export(request):
    attendee_resource = AttendeeResource()
    dataset = attendee_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attatchent; filename="attendees.xls"'
    return response
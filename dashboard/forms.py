import logging

from django.utils.safestring import mark_safe
from django import forms
from api_v1.models import Attendee
log = logging.getLogger("{}.*".format(__package__))



class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = "__all__"
        exclude = ('created_at', 'updated_at', 'ticket')


    def clean(self):
        """
        Checks for dulicate Attendees (email, phone_numner)
        """
        if not self.instance.pk:
            print("lalallala {}".format(self.instance.pk))
            ok = True
            email = self.cleaned_data.get("email", False)
            phone = self.cleaned_data.get("phone_number", False)

            dup_email = Attendee.objects.filter(email=email)
            dup_num = Attendee.objects.filter(phone_number=phone)

            if dup_email:
                ok = False      
                log.warning("Email already in use")
                self._errors["email"] = [mark_safe("Email already in use")]
            if dup_num:
                ok = False
                log.warning("Phone number already in use")
                self._errors["phone"] = [mark_safe("Phone number already in use")]

            return self.cleaned_data if ok else None


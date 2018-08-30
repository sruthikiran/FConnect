from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo,Checklist


CHOICES = ('Completed', 'Not Completed', 'Not Applicable')

class RegistrationForm(forms.ModelForm):
    re_password = forms.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['username','email','password','re_password']

# class ChecklistForm(forms.ModelForm):
#         application = forms.ChoiceField(required=False,choices=CHOICES)
#         test_scores = forms.ChoiceField(required=False,choices=CHOICES)
#         school_transcript = forms.ChoiceField(required=False,choices=CHOICES)
#         reports = forms.ChoiceField(required=False,choices=CHOICES)
#         sec_school_reports = forms.ChoiceField(required=False,choices=CHOICES)
#         recommenadtion = forms.ChoiceField(required=False,choices=CHOICES)
#         class Meta:
#             model = Checklist
#             fields = ['application','test_scores','school_transcript','reports','sec_school_reports','recommenadtion',]

# class ProfileForm(forms.ModelForm):
#     firstName = forms.CharField(max_length=128)
#     lastName = forms.CharField(max_length=128)
#     class Meta:
#         model = UserProfileInfo
#         fields = ['firstName','lastName','gender','birthday','address','city','state','schoolState','major','schoolName']

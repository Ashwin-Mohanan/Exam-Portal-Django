from django import forms
from django.contrib.auth.models import User

# from DjangoLogin.testapp.models import Q
from testapp.models import Q
class RegistrationUser(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')

class ans_form(forms.ModelForm):
    class Meta:
        model=Q
        fields=('Qta1','op1','op2','op3','op4')
#         

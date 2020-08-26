from django import forms

from myuser.models import MyUser

class Signup_Form(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["username", "password", "age"]
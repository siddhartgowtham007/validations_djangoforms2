from app.models import *
from django import forms



class Employeeform(forms.Form):
    Eid=forms.IntegerField()
    Ename=forms.CharField()
    Erole=forms.CharField()
    Ecatch=forms.CharField(required=False,widget=forms.HiddenInput)

    def Ecatc(self):
        A=self.cleaned_data['Ecatch']
        if len('A')>0:
            raise forms.ValidationError('bot')

from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse


def clean_element(request):
    EEFO=Employeeform()
    d={'EEFO':EEFO}

    if request.method=='POST':
        SFO=Employeeform(request.POST)
        if SFO.is_valid():
            ei=SFO.cleaned_data['Eid']
            en=SFO.cleaned_data['Ename']
            er=SFO.cleaned_data['Erole']
            SO=Employee.objects.get_or_create(Eid=ei,Ename=en,Erole=er)[0]
            SO.save()
            return HttpResponse('DETAIS_INSERTED')
        else:
            return HttpResponse('invaloid data')
            

    return render(request,'oner.html',d)
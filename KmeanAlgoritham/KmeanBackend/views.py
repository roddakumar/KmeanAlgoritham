from django.shortcuts import render
from django.shortcuts import render, redirect 
from django import forms
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os



def index(request):
    if request.method == "POST": 
     return index2(request.File)
    else :
      ## return HttpResponse("Fuck")
        return render(request,'fileView.html') 


def index2(request):
 # v=request.File["filename"]
 form = upload_file(request)
 print(form)
 return HttpResponse(form)


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)





class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        handle_uploaded_file(request.FILES['file'])
        form = UploadFileForm()
    return HttpResponse("sucess")
from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):

    form = SubscriberForm(request.POST or None)
    if request.POST :#and form.is_valid():
        print(request.POST)
       # print(form.cleaned_data)

        new_form = form.save()

    return render(request,'landing/landing.html',locals())

def home(request):



    return render(request,'landing/home.html',locals())
from django.shortcuts import render,redirect
from .forms import UrlForm
from .models import *
import uuid


def home(request):
    form = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            if ("http://" not in original_url) and ("https://" not in original_url) :
                original_url = "http://" + original_url
            uid = str(uuid.uuid4())[:6]
            new_url = Url(original_url=original_url, short_url=uid)
            new_url.save()
            context={'uid':uid}
            return render(request,'base/home.html',context)

    context  = {"form": form}
    return render(request, 'base/home.html', context)


def final(request, pk):
    url_details = Url.objects.get(short_url=pk)
    return redirect(url_details.original_url)

from django.shortcuts import render,redirect
from .forms import ShortLinkForm
from .models import ShortLink
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib import admin
# Create your views here.


def home(request):
    context = {}
    context["form"] = ShortLinkForm()
    if request.method == "POST":
        user_form = ShortLinkForm(request.POST)
        if user_form.is_valid():
            data = user_form.save() # when form will save that time it will go to model and do the all operation of save funciton , generate_short_url function 
            new_link= request.build_absolute_uri("/")+data.short_url
            context["new_link"] = new_link
            context["long_link"] = data.long_url
            context["short_link"]= data.short_url
        else : 
            context["error"] = user_form.errors
            
    return render(request,"home.html",context)



def redirect_url(request,shortest_part):
    #if it finds admin into the shorted code, then it can occure conflict . to avoid conflict we are redirect to the admin url if we find admin word inside shortest_part
    if shortest_part =="admin":
        return admin.site.urls
    
    try:
        short = ShortLink.objects.get(short_url=shortest_part)
        short.times_followed +=1 #it will increase times_followed variable for each click on link
        short.save()
        return HttpResponseRedirect(short.long_url)
    except ShortLink.DoesNotExist:
        raise Http404("sorry, this link is broken")
    



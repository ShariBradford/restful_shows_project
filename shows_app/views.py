from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from datetime import datetime
from django.contrib import messages

# Create your views here.

time_format = '%Y/%m/%d %I:%M %p'

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "shows": Show.objects.all(),
    }
    return render(request,'shows.html', context)

def new_show(request):
    return render(request, 'create.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0: 
        for k,v in errors.items():
            messages.error(request,v)
        return redirect('/shows/new')
        
    elif len(Show.objects.filter(title__iexact = request.POST["show_title"])) > 0:
        messages.error(request, "Show title must be unique.")
        return redirect('/shows/new')

    else:
        new_show = Show.objects.create(
            title=request.POST["show_title"], 
            network=request.POST["show_network"],
            desc=request.POST["show_description"], 
            release_date=request.POST["release_date"])
        return redirect(f"/shows/{new_show.id}")

def display_show(request,show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        "id": this_show.id,
        "title": this_show.title,
        "network": this_show.network,
        "desc": this_show.desc,
        "release_date": this_show.release_date,
        "updated_at": this_show.updated_at,
    }
    return render(request, 'display.html',context)

def destroy_show(request,show_id):
    this_show = Show.objects.get(id=show_id)
    this_show.delete()
    return redirect('/shows')

def edit_show(request,show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        "id": this_show.id,
        "title": this_show.title,
        "network": this_show.network,
        "desc": this_show.desc,
        "release_date": this_show.release_date,
        "updated_at": this_show.updated_at,
    }
    return render(request, 'edit.html',context)

def update_show(request,show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0: 
        for k,v in errors.items():
            messages.error(request,v)
        return redirect(f"/shows/{show_id}/edit")

    elif len(Show.objects.filter(title__iexact = request.POST["show_title"]).exclude(id=show_id)) > 0:
        messages.error(request, "Show title must be unique.")
        return redirect('/shows/new')
        
    else:
        this_show = Show.objects.get(id=show_id)
        this_show.title=request.POST["show_title"]
        this_show.network=request.POST["show_network"]
        this_show.desc=request.POST["show_description"]
        this_show.release_date=request.POST["release_date"]
        this_show.save()
        return redirect(f"/shows/{this_show.id}")


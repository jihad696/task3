from django.http import HttpResponse
from django.shortcuts import render

def list_view(req):
    trainees = [
        [1, "Ahmed"],
        [2, "Sara"],
        [3, "Mohamed"],
    ]
    return render(req, "trainee/list.html", {"trainees": trainees})

def add_view(req):
    return render(req, "trainee/new.html")

def update_view(req, id):
    return HttpResponse(f"Update Trainee {id}")

def delete_view(req, id):
    return HttpResponse(f"Delete Trainee {id}")

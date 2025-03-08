from django.http import HttpResponse
from django.shortcuts import render

tracks = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "PHP"},
    {"id": 3, "name": "Java"},
]


def Listview(req):
    return render(req, "track/list.html", context={"tracks": tracks})


def Addview(req):
    return render(req, "track/new.html")


def Updateview(req, id):
    track = next((t for t in tracks if t["id"] == id), None)
    if track:
        return HttpResponse(f'<h1>Update Track: {track["name"]}</h1>')
    return HttpResponse("<h1>Track Not Found</h1>")




def Deleteview(req, id):
    global tracks
    tracks = [t for t in tracks if t["id"] != id]
    return HttpResponse(f"<h1>Deleted Track {id}</h1>")

from django.urls import path
from .views import Listview, Addview, Updateview, Deleteview

urlpatterns = [
    path("", Listview, name="track_list"),
    path("add/", Addview, name="add_track"),
    path("update/<int:id>/", Updateview, name="update_track"),
    path("delete/<int:id>/", Deleteview, name="delete_track"),
]

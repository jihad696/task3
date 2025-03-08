from django.urls import path
from .views import *

urlpatterns = [
    path("", list_view, name="trainees"),
    path("add/", add_view, name="trainee_new"),
    path("update/<int:id>/", update_view, name="trainee_update"),
    path("delete/<int:id>/", delete_view, name="trainee_delete"),
]



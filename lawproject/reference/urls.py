from django.urls import path

from . import views

app_name = "reference"
urlpatterns = [
    path("", views.do_nothing, name="index")
]

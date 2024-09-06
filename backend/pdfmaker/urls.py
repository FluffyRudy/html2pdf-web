from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view),
    path("api/", views.home_view, name="home"),
    path("api/createpdf/", views.HTMLToPDFMaker.as_view(), name="create-pdf"),
]

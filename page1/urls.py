from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

from django.views.generic.list import ListView

urlpatterns = [
    path("", views.IndexViewClass.as_view(),name="indeks"),
    path("coba/",views.IndexViewClass.as_view(),name="IndexViewClass"),
    path("coba/<str:parameter>",views.Parameterku.as_view(),name="Parameterku"),
]

urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

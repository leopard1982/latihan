from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.indeks,name="indeks"),
    path("read/<str:yangmana>/", views.read_article,name="read_article"),
    path("b/i/",views.Insert_InputMyBlog,name="Insert_InputMyBlog"),
    path("b/d/<str:judul>/",views.Delete_InputMyBlog,name="Delete_InputMyBlog"),
    path('login/',views.LoginUser,name="LoginUser"),
    path('logout/',views.LogoutUser,name="LogoutUser")
]

urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

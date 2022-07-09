from django.contrib import admin
from django.urls import path
from kc_app.views import home,courses,acheivements,feedback,centers

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("acheivements/",acheivements,name="acheivements"),
    path("courses/",courses,name="courses"),
    path("feedback/",feedback,name="feedback"),
    path("centers/",centers,name="centers"),
]

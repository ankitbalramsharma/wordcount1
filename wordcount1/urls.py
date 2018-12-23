#from django.contrib import admin
from django.urls import path
from . import views     # . means from current directory

urlpatterns = [
    # path('page1/', admin.site.urls),
    path('',views.homepage, name='home'),
    path('count/',views.count, name='count'),
    path('aboutUs',views.about, name='about'),


]

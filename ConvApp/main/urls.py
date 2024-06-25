
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='onas'),
    #path('download_gcode/<str:gcode_file_name>', views.download_gcode, name='download_gcode'),
]
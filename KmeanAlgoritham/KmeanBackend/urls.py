from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index2', views.index2, name='index2') ,# upload_file
    path('upload_file', views.index2, name='upload_file')
      
]
from django.urls import path
from . import views

# Url patterns for after people/ or just ''
urlpatterns = [
    path('', views.home, name ='home'),
    path('<int:people_id>', views.about, name = 'about'),
    path('make', views.make, name ='make'),
    ]

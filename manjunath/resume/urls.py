from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('someview', views.some_view, name='someview'),
    path('view', views.fetch_data, name='view'),
    path('save', views.save, name='save'),
]

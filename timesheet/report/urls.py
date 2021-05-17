from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('data/<int:id>/<str:start_date>/<str:end_date>', views.data, name='data'),
     path('data/<int:id>/<str:start_date>', views.data, name='data'),

     path('data/<int:id>', views.data, name='data'),
]
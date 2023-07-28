from .import views
from django.urls import path

urlpatterns = [

    path('',views.develop,name='develop')

   # path('',views.demo,name='demo'),
   # path('add/',views.operations,name='operations')


]

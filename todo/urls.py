from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add/',views.add,name='add'),


    path('delete/<int:taskId>',views.delete,name='delete'),
    path('edit/<int:taskId>',views.edit,name='edit'),
    path('complete/<int:taskId>',views.complete,name='complete'),
    path('uncomplete/<int:taskId>',views.uncomplete,name='uncomplete'),


]
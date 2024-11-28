from django.urls import path
from . import views
urlpatterns = [
    path('',views.parrot,name='list'),
    path('2',views.list,name='task'),
    path('3/<int:pk>',views.task,name='details'),
    path('4/<int:pk>',views.display,name='ludo'),
    path('5',views.oops,name='program')
]
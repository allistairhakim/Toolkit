from django.urls import path, include
from . import views #. means the current dir


urlpatterns = [
    path('', views.home, name="gadgets-home"),
    path('about/', views.about, name="gadgets-about"),
    path('todo/', views.todo, name="gadgets-todo"),
    path(r'^delete/(?P<pk>[0-9]+)/$', views.todo_delete, name='todo_delete'),
]

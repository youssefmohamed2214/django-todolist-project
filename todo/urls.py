from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('settings/', views.settings_page, name='settings_page'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]
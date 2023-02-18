from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, RegisterUser

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='delete-task'),

    ]
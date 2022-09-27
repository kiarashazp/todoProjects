from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('delete/<int:todo_id>', views.DeleteTask.as_view(), name='delete_task'),
    path('update/<int:todo_id>', views.UpdateTask.as_view(), name='update_task'),
    path('detail/<int:todo_id>', views.DetailTask.as_view(), name='detail_task'),
]

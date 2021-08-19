from django.urls import path

from .views import  TaskView, TaskDetailView, TaskEditView, TaskDeleteView,DeleteNotification, AssignTaskToView,AssignTaskView,AdminDemoLoginView,DeveloperDemoLoginView,PmDemoLoginView,SubmitterDemoLoginView

app_name = 'core'

urlpatterns = [
    path('', TaskView.as_view(), name='task'),
    path('edit/<int:pk>/',TaskEditView.as_view(), name='task_edit'),
    path('delete/<int:pk>/',TaskDeleteView.as_view(), name='task_delete'),
    path('delete_notification/<int:pk>/',DeleteNotification.as_view(), name='notification_delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/',AssignTaskView.as_view(), name='task_response_form'),
    path('task_assigned_to/<int:pk>/',AssignTaskToView.as_view(), name='task_assigned_to'),

    # DEMO ACCOUNT PATHS ###
    path('submitter_demo/', SubmitterDemoLoginView.as_view(), name='submitter_demo'),
    path('pm_demo/', PmDemoLoginView.as_view(), name='pm_demo'),
    path('developer_demo/', DeveloperDemoLoginView.as_view(), name='dev_demo'),
    path('administrator_demo/', AdminDemoLoginView.as_view(), name='admin_demo'),
]
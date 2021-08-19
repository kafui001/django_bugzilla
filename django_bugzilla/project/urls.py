from django.urls import path


app_name = 'project'

from .views import ProjectHomeView,ProjectFormView,ProjectEditView,ProjectDeleteView,ProjectDetailView,AssignProjectView

urlpatterns = [
    path('',ProjectHomeView.as_view(), name='project_home'),
    path('project_form/',ProjectFormView.as_view(), name='project_form'),
    path('edit/<int:pk>/',ProjectEditView.as_view(), name='project_edit'),
    path('delete/<int:pk>/',ProjectDeleteView.as_view(), name='project_delete'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/',AssignProjectView.as_view(), name='project_response_form'),
]
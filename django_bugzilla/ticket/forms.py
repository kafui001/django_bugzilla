import random

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import ProjectManager, Developer, Task, 
from core.models import Ticket,TaskPriority, TaskStatus, Comment,Developer, Project


assign_developers = Developer.objects.all().values_list('username','username')
dev_list = []
for item in assign_developers:
    dev_list.append(item)



project_choices = Project.objects.all().values_list('title','title')
project_list = []
for item in project_choices:
    project_list.append(item)    


priority_choices = TaskPriority.objects.all().values_list('name','name')
priority_choice_list = []
for item in priority_choices:
    priority_choice_list.append(item)


status_choices = TaskStatus.objects.all().values_list('name','name')
status_choice_list = []
for item in status_choices:
    status_choice_list.append(item)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'priority',
            'project',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',                            
                'placeholder':'title of your ticket',
                'id':"ticketForm1"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'details of the issue',
                'id':"ticketForm2",
                'rows':"5"
                }
            ),
            'priority': forms.Select(choices=priority_choice_list, attrs={
                'class': 'form-control',
                'id':'ticketForm3',
                'aria-label':"Default select Priority",
                }
            ),
            'project': forms.Select(choices=project_list, attrs={
                'class': 'form-control',
                'id':'ticketForm4',
                'aria-label':"Default select Project",
                }
            )
        }


class TicketEditForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'status',
            'priority',
            'project',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',                            
                'placeholder':'title of your ticket',
                'id':"ticketForm1"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'add any extra details here',
                'id':"ticketForm2",
                'rows':"5"
                }
            ),
            'priority': forms.Select(choices=priority_choice_list, attrs={
                'class': 'form-control',
                'id':'ticketForm3',
                'aria-label':"",
                }
            ),
            'status': forms.Select(choices=status_choice_list, attrs={
                'class': 'form-control',
                'id':'ticketForm4',
                'aria-label':"",
                }
            ),
            'project': forms.Select(choices=project_list, attrs={
                'class': 'form-control',
                'id':'ticketForm5',
                'aria-label':"",
                }
            )

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body',
        ]

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Leave a comment here',
                'id':"commentForm",
                'rows':"5"
                }
            )

        }


class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = [
            'username'
        ]

        widgets = {
            'username': forms.Select(choices=dev_list, attrs={
                'class': 'form-control',
                'id':'DeveloperForm',
                'aria-label':"",
                }
             )
        }
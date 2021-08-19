from django import forms
from core.models import Task, Ticket, ProjectManager, Developer,Project, ProjectStatus


progress = (
    (0,0),(5,5),(10,10),(15,15),(20,20),
    (25,25),(30,30),(35,35),(40,40),
    (45,45),(50,50),(55,55),(60,60),
    (65,65),(70,70),(75,75),(80,80),
    (85,85),(90,90),(95,95),(100,100)
    )


project_status_choices = ProjectStatus.objects.all().values_list('name','name')
choice_list = []
for item in project_status_choices:
    choice_list.append(item)



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
           'description',
           'begin_date',
           'end_date',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',                            
                'placeholder':'title of your project',
                'id':"exampleFormControlInput77"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',

                'placeholder':'add any extra details here',
                'id':"exampleFormControlTextarea78",
                'rows':"5"
                }
            ),
            # 'status': forms.Select(choices=status_choice_list, attrs={
            #     'class': 'form-control',
            #     'id':'formFileMultipleone',
            #     'aria-label':"",
            #     }
            # ),
            'begin_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'title',
            'description',
            'status',
            'completion',
            'begin_date',
            'end_date'
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
            'status': forms.Select(choices=choice_list, attrs={
                'class': 'form-control',
                'id':'ticketForm3',
                'aria-label':"",
                }
            ),
            'completion': forms.Select(choices=progress, attrs={
                'class': 'form-control',
                'id':'ticketForm4',
                'aria-label':"",
                }
            ),
            'begin_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),

        }
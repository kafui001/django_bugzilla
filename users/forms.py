from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from core.models import BugUser, Administrator, ProjectManager, Developer, AllImage

# assign_admin = BugUser.objects.filter(is_superuser=False).values_list('username','username')
# admin_list = []
# for user in assign_admin:
#     admin_list.append(user)



# assign_pm = BugUser.objects.filter(is_project_manager=False).values_list('username','username')
# pm_list = []
# for user in assign_pm:
#     pm_list.append(user)


# # feature for assigning developer to a ticket in ticket_detail.html
# assign_dev_ticket = BugUser.objects.filter(is_developer=True).values_list('username','username')
# dev_ticket_list = []
# for user in assign_dev_ticket:
#     dev_ticket_list.append(user)

# assign_dev = BugUser.objects.filter(is_developer=False).values_list('username','username')
# dev_list = []
# for user in assign_dev:
#     dev_list.append(user)


# get_pm = BugUser.objects.filter(is_project_manager=True).values_list('username','username')
# get_pm_list = []
# for user in get_pm:
#     get_pm_list.append(user)

class UserSignUpForm(UserCreationForm):
    email       = forms.EmailField()
    first_name  = forms.CharField(max_length=100)
    last_name   = forms.CharField(max_length=100)
    
    class Meta:
        model = BugUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        fields = [
            'username',
           'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'type':"email",
                'class': 'form-control form-control-lg' ,                            
                'placeholder':'username',
                }
            ),
            
            'password': forms.TextInput(attrs={
                'type':"password",
                'class': 'form-control form-control-lg' ,                            
                'placeholder':'***************',
                # 'id':"exampleFormControlInput77"
                }
            )
        }


# class AdminForm(forms.ModelForm):
#     class Meta:
#         model  = Administrator
#         fields = ['username']

        # widgets = {
        #     'admin': forms.Select(choices=admin_list, attrs={
        #         'class': 'form-control',
                
        #         }
        #     ),
        # }


# class DevForm(forms.ModelForm):
#     class Meta:
#         model  = Developer
#         fields = ['username']

#         widgets = {
#             'username': forms.Select(choices=dev_list, attrs={
#                 'class': 'form-control',
#                 }
#             )
#         }


# # feature for assigning developer to a ticket in ticket_detail.html
# class DevTicketForm(forms.ModelForm):
#     class Meta:
#         model  = Developer
#         fields = ['username']

#         widgets = {
#             'username': forms.Select(choices=dev_ticket_list, attrs={
#                 'class': 'form-control',
#                 }
#             )
#         }

# class PmForm(forms.ModelForm):
#     class Meta:
#         model  = ProjectManager
#         fields = ['username']

#         widgets = {
#             'username': forms.Select(choices=pm_list, attrs={
#                 'class': 'form-control',
#                 }
#             ),
#         }
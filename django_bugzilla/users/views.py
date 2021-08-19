from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView,View, TemplateView
from django.contrib.auth import login
from django.views import View


from .forms import UserSignUpForm, LoginForm
from core.mixins import SigninRequiredMixin, OnlyAdminAllowedMixin,SubmitterAndDevNotAllowedMixin,SubmitterNotAllowedMixin
from core.models import Administrator, BugUser,Developer, ProjectManager, Notification

class UserSignUpView(View):
    
    def get(self, request, *args, **kwargs):
        form = UserSignUpForm()
        return render(request, "users/signup.html", { 'form': form })

    def post(self, request, *args, **kwargs):

        form = UserSignUpForm(self.request.POST)

        if form.is_valid():
            # save the user form and log the user in
            user          = form.save(commit=False)
            user.email    = form.cleaned_data["email"]
            user.username = form.cleaned_data["username"]
            user.save()
            login(request, user)
            return redirect('core:task')
        else:
            return render(request, "users/signup.html", {
                'form': form
            })


class UserLogin(FormView):
    template_name = "users/signin.html"
    form_class  = LoginForm
    success_url = reverse_lazy("core:task")

    def post(self, request, *args, **kwargs):
        form     = self.get_form()
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)








class RoleView(SigninRequiredMixin,SubmitterAndDevNotAllowedMixin,View):
    def get(self, request, *args,**kwargs):
        non_dev   = BugUser.objects.filter(is_developer=False)
        non_pm    = BugUser.objects.filter(is_project_manager=False)
        non_admin = BugUser.objects.filter(is_superuser=False)
        context = {
            'non_dev' : non_dev,
            'non_pm' : non_pm,
            'non_admin' : non_admin
        }
        return render(request,'users/roles.html',context)

    def post(self, request, *args,**kwargs):
        if self.request.POST['ad'] != 'none':
            ad_id = self.request.POST['ad']
            
            user  = BugUser.objects.get(id=ad_id)
            
            for item in Administrator.objects.all():
                if item != user.id:
                    user.is_superuser=True
                    user.save()

                    ad_user = Administrator.objects.create(
                        username = user
                    )

                    Notification.objects.create(
                        notification_type   = 6,
                        to_user             = user,
                        from_user           = self.request.user,
                        admin_role_assign   = ad_user
                    )

                    return redirect('roles_home')
            return redirect('roles_home')


class PmPostView(View):
    def post(self, request, *args,**kwargs):
        if self.request.POST['pm'] != 'none':
            pm_id = self.request.POST['pm']
            user = BugUser.objects.get(id=pm_id)
            
            user.is_project_manager=True
            user.save()
            
            ad_user = self.request.user
            pm_user = Administrator.objects.get(username=ad_user)
            
            a_pm_user = ProjectManager.objects.create(
                        username = user,
                        admin    = pm_user
                    )

            Notification.objects.create(
                    notification_type = 5,
                    to_user           = user,
                    from_user         = self.request.user,
                    pm_role_assign    = a_pm_user
                )
            
            return redirect('roles_home')
        return redirect('roles_home')

class DevPostView(View):
    def post(self, request, *args,**kwargs):
        if self.request.POST['dev'] != 'none':
            dev_id = self.request.POST['dev']
            
            user = BugUser.objects.get(id=dev_id)
            user.is_developer=True
            user.save()
            
            dev_assigner = self.request.user
            assigner     = BugUser.objects.get(id=dev_assigner.id)

            a_user = Developer.objects.create(
                        username    = user,
                        assigner    = assigner
                    )

            Notification.objects.create(
                    notification_type = 4,
                    to_user           = user,
                    from_user         = self.request.user,
                    dev_role_assign   = a_user
                )
                    
            return redirect('roles_home')
        return redirect('roles_home')


class AssignPmRoleView(SigninRequiredMixin,SubmitterAndDevNotAllowedMixin,TemplateView):
    template_name = 'users/assigned_pm_Role.html'


class AssignDevRoleView(SigninRequiredMixin,SubmitterNotAllowedMixin,TemplateView):
    template_name = 'users/assigned_dev_role.html'


class AssignAdminRoleView(SigninRequiredMixin,OnlyAdminAllowedMixin,TemplateView):
    template_name = 'users/assigned_admin_role.html'


class ProjectPmRoleView(SigninRequiredMixin,SubmitterNotAllowedMixin,TemplateView):
    template_name = 'users/project_pm_Role.html'


class PageNotPermittedView(SigninRequiredMixin,TemplateView):
    template_name = "users/page_not_permitted.html"


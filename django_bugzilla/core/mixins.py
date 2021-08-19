from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class SigninRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        print(request.user.is_authenticated)
        return super().dispatch(request, *args, **kwargs)


class OnlyAdminAllowedMixin(object):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        print('#######')
        print('HigherLevel')
        if not request.user.is_superuser:
            print('inside HigherLevel')
            return redirect('not_permitted')
        return super().dispatch(request, *args, **kwargs)


class PmLevelMixin(object):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        print('#######')
        print('PmLevel')
        if not request.user.is_project_manager and not request.user.is_superuser:
            print('inside PmLevel')
            print(request.user.is_project_manager)
            print(request.user.is_superuser)
            return redirect('not_permitted')
        print('outside PmLevel')
        print(request.user.is_project_manager)
        return super().dispatch(request, *args, **kwargs)


class SubmitterAndDevNotAllowedMixin(object):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_project_manager and not request.user.is_superuser:
            return redirect('not_permitted')
        return super().dispatch(request, *args, **kwargs)


class SubmitterNotAllowedMixin(object):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_developer and not request.user.is_project_manager and not request.user.is_superuser:
            return redirect('not_permitted')
        return super().dispatch(request, *args, **kwargs)
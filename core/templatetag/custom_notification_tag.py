from django import template
from core.models import Notification

# template_tag is registered in dj_bugs/settings.py under TEMPLATES
register = template.Library()


@register.inclusion_tag('core/notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(to_user=request_user).exclude(notification_is_seen=True).order_by('-date_created')
    notification_count = Notification.objects.filter(to_user=request_user).count()
    return {'notifications': notifications,'notification_count': notification_count}


@register.inclusion_tag('core/notifications.html', takes_context=True)
def notifications_count(context):
    request_user = context['request'].user
    notification_count = Notification.objects.filter(to_user=request_user).count()
    return {'notification_count': notification_count}
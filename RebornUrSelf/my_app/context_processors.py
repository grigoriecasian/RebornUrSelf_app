from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        recent = Notification.objects.filter(user=request.user)[:10]
        unread = Notification.objects.filter(user=request.user, is_read=False).count()
        return {
            'recent_notifications': recent,
            'unread_notif_count': unread,
        }
    return {}

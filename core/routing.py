from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from messager.consumers import MessagerConsumer
from notifications.consumers import NotificationsConsumer

# from bootcamp.notifications.routing import notifications_urlpatterns
# from bootcamp.messager.routing import messager_urlpatterns

application = ProtocolTypeRouter(
    {
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    [
                        re_path(r"^notifications/$", NotificationsConsumer.as_asgi()),
                        re_path(r"^(?P<username>[^/]+)/$", MessagerConsumer.as_asgi()),
                    ]
                )
            )
        )
    }
)

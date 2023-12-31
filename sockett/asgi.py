import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import sockett.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sockett.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        sockett.routing.websocket_urlpatterns
    ),
})
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from socketapis.consumers import MyConsumer

application = ProtocolTypeRouter(
   {
       'http': get_asgi_application(),
       'websocket': AuthMiddlewareStack(
           URLRouter(
               [
                   path('ws/mysocket/', MyConsumer.as_asgi()),
               ]
           )
       ),
   }
)
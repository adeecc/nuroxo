from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path
from django.urls.conf import include

schema_view = get_schema_view(
    openapi.Info(
        title="Backend for the Nuroxo: The AI Chatbot",
        default_version='v1',
        description="API End Points for the Nuroxo",
        terms_of_service=None,
        contact=openapi.Contact(email='adi.chopra108@gmail.com'),
        license=openapi.License(name="Private Property")
    ),
    public=True, 
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/chatbot/', include('chatbot.urls'))
]

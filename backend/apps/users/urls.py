"""Users app urls"""
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('apps.users.api.v1.urls'))
]

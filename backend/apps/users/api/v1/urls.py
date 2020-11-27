"""API users v1 urls"""

# Django
from django.urls import path

# Views
from apps.users.api.v1.views import NewUserView, SetNewPasswordView, MakeRaffleView

urlpatterns = [
    path('new-user/', NewUserView.as_view(), name='new-user'),
    path('change-password/<str:token>/', SetNewPasswordView.as_view(), name='change-password'),
    path('winner/', MakeRaffleView.as_view(), name='winner'),
]

from django.urls import path
from .views import profiles,login_user

urlpatterns = [
    path('', profiles, name='profiles'),
    path('ad/', login_user, name='login_user')
]
from django.urls import path
from account.views import index, login_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login')
]

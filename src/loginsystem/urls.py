from django.urls import path
from .views import index, loginuser, xyz, autocomplete_user_name

app_name = 'loginsystem'

urlpatterns = [
    path('', index, name='index'),
    path('login/', xyz, name='xyz'),
    path('userhome', loginuser, name='loginuser'),
    path('autocomplete_user_name/', autocomplete_user_name, name='autocomplete_user_name'),
]

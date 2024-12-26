from django.urls import path
from .views import Home

app_name = 'MovieApp'

urlpatterns = [
    path('', Home, name='home'),

]
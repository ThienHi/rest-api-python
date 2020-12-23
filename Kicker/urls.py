from django.urls import path
from . import views


app_name = 'kicker'
urlpatterns = [
    path('', views.infoKicker.as_view(), name='info'),
]

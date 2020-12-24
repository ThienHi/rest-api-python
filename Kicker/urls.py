from django.urls import path
from . import views


app_name = 'kicker'
urlpatterns = [
    path('', views.infoKicker.as_view(), name='info'),
    path('<int:pk>/', views.KickerInfo.as_view(), name='kickers'),
    path('mixins/', views.KickerMixin.as_view(), name='mixins'),
]

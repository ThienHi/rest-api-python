from django.urls import path
from . import views

app_name = 'snippet'
urlpatterns = [
    path('', views.snippet_list, name='snippet'),
    path('<int:pk>/', views.snippet_detail)
]

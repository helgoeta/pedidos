from django.urls import path
from project_api import views


urlpatterns = [
    path('test-hello/', views.HelloApiView.as_view()),
]

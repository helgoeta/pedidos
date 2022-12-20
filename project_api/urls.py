from django.urls import path
from project_api import views


urlpatterns = [
    path('test-hello/', views.HelloApiView.as_view()),
    path('clientes', views.view_clientes, name='all-clientes'),
    path('clientes/', views.add_cliente, name='add-cliente'),
    path('clientes/<int:pk>', views.update_clientes, name='update_clientes')
]

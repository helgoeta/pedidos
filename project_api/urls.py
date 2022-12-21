from django.urls import path
from project_api import views


urlpatterns = [
    path('test-hello/', views.HelloApiView.as_view()),
    path('clientes', views.view_clientes, name='all-clientes'),
    path('clientes/', views.add_cliente, name='add-cliente'),
    path('clientes/<int:pk>', views.update_clientes, name='update_clientes'),
    path('produtos', views.view_produtos, name='view_produtos'),
    path('produtos/', views.add_produto, name='add_produto'),
    path('produtos/<int:pk>', views.update_produto, name='update_produto'),
    path('pedidos', views.view_pedidos, name='view_pedidos'),
    path('pedidos/', views.add_pedido, name='add_pedido'),
    path('pedidos/<int:pk>', views.update_pedido, name='update_produto')
]

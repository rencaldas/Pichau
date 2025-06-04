from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar/', views.gerenciar_clientes, name='gerenciar_clientes'),
    path('deletar/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('gerenciar/', views.gerenciar_clientes, name='gerenciar_clientes'),
    path('deletar/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
]


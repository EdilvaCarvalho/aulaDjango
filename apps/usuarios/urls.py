from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('atualiza_usuario', views.atualiza_usuario, name='atualiza_usuario'),
    path('edita_usuario', views.edita_usuario, name='edita_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
from django.urls import path
from . import views

urlpatterns = [
    path("register",views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name='logout'),
    path("createD",views.createD,name='createD'),
    path("listar",views.listar,name='listar'),
    path("delete/<id>/",views.delete,name='delete'),
    path("actualizar/<id>",views.actualizar,name='actualizar'),
    path("modificar/<id>",views.modificar,name='modificar')
]

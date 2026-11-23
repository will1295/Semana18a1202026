from django.urls import path
from . import views

urlpatterns=[
    path("",views.inicio_view,name="inicio"),
    path("login/",views.login_view,name="login"),
    path("registro/",views.registro_view,name="registro"),
    path("logout/",views.logout_view,name="logout"),
    path("visitar/",views.visitar,name="visitar"),
    path("guardar/<str:nombre>/",views.guardar_usuario,name="guardar_usuario"),
    path("ver/",views.ver_sesion,name="ver_sesion"),
    path("limpiar/",views.limpiar_session,name="limpiar_sesion"),
]
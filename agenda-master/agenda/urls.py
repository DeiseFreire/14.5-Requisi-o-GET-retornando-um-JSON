
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/<int:id_usuario>/', views.json_lista_evento),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>', views.delete_evento),
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.login_user),
    path('login/auth', views.submit_login),
    path('logout/', views.logout_user)

]

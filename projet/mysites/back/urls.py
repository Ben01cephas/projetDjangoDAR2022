from django.conf import settings
from back import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from back.views import *

from back.views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('apropos', views.aPropos, name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('accounts/new', views.create_user,name='inscription'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='connexion.html')),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='connexion.html')),
    path('accounts/profile', views.homeUser, name='homeUser'),
    path('accounts/profile/delete/<int:pk>', views.delete_epreuve, name='delete_epreuve'),
    path('accounts/profile/epreuve/<int:pk>', views.epreuve_view, name='epreuve_view'),
    path('accounts/profile/correction/<int:pk>', views.correction_view, name='correction_view'),
    path('compte', login_required(update_user),name='update'),
    path('password/', login_required(changePassword_user),name='password'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

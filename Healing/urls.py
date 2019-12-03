"""Healing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from blog.views import base, mantenedor
from blog.usuarios.views import Login, logoutUsuario, registro_usuario
from blog.usuarios.api import UserAPI
from django.conf.urls import url, include
from rest_framework import routers
from blog.usuarios import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUsuario), name='logout'),
    path('api/1.0/create_user/', UserAPI.as_view(), name='api_create_user'),
    path('singup/', registro_usuario, name='singup'),
    path('mantenedor/', login_required(mantenedor), name='mantenedor'),
    url(r'^service/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(('blog.urls', 'blog'))),
    path('', base, name='inicio'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='blog/registration/password_reset_form.html',
                                                           email_template_name="blog/registration/password_reset_email.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(
        template_name='blog/registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(
        template_name='blog/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(
        template_name='blog/registration/password_reset_complete.html'), name='password_reset_complete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



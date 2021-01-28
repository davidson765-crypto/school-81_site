"""myfirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
#from register import views as v
from django.contrib.auth import views as authViews
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView




urlpatterns = [
    #path('', include("django.contrib.auth.urls")), 
    #path("register/", v.register, name='register'),
    
    #path('done/',PasswordChangeDoneView.as_view(template_name='registration/change_done.html'), name='password_change_done'), 
    #path('change/', PasswordChangeView.as_view(template_name='registration/change.html'), name='change'), 
    #path('exit/', authViews.LogoutView.as_view(), name='exit'),
    #path('login/', LoginView.as_view(), name='login'),

    #path('register/', include('register.urls')), 
    path('', include('articles.urls')), 
    #path('add/', include('articles.urls')), 
    path('article/', include('articles.urls')), 
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]

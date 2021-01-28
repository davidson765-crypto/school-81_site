from django.urls import path

from . import views

app_name='articles'
urlpatterns=[
    path("theme", views.theme, name="theme"), 
    path('confirm_email/', views.confirm_mail, name='confirm_mail'),
    path('del/', views.del_at, name='del_at'), 
    path('other/', views.other, name='other'), 
    path('profile/', views.profile, name='profile'),
    path('', views.signup, name='signup'), 
    path('logout/', views.log_out, name='log_out'), 
    path('login/', views.log_in, name='log_in'), 
    path('filt/', views.filt, name='filt'), 
    path('list/', views.index, name='index'), 
    path('<int:user_id>/', views.detail, name='detail'),
    ]
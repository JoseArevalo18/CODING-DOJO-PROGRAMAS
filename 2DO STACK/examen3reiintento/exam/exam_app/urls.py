from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),#0
    path('user/create_user', views.create_user),#1
    path('user/dashboard', views.dashboard),#2
    path('user/login', views.login),#3
    path('user/logout', views.logout),#4
    path('wish/new',views.dashboard),#5
    path('wish/create', views.addShow),#6
    path('wish/',views.displayShow),#7
    path('wish/<int:number>', views.showInfo),#8
    path('wish/<int:number>/edit', views.editShow),#9
    path('wish/update/<int:number>',views.editShow),
    path('wish/<int:number>/delete',views.delete_show),#10
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),#0
    path('user/create_user', views.create_user),#1
    path('user/dashboard', views.dashboard),#2
    path('user/login', views.login),#3
    path('user/logout', views.logout),#4
    path('user/<int:user_id>', views.user_page),#5
    path('wishes/create', views.create_group),#6
    path('wishes/group_form', views.group_form),#7
    path('wishes/<int:group_id>', views.show_group),#8
    path('wishes/add_review', views.add_review),#9
    path('review/<int:review_id>/delete', views.delete_review)
]

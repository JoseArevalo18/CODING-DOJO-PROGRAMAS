from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/<int:user_id>', views.user_page),
    path('group/create', views.create_group),
    path('group/group_form', views.group_form),
    path('group/<int:group_id>', views.show_group),
    path('group/add_review', views.add_review),
    path('review/<int:review_id>/delete', views.delete_review)
]
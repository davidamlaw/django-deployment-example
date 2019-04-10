from django.urls import path
from . import views

# Template Tagging
app_name = 'app_two'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('relative/', views.relative, name='relative_urls'),
    # path('users/', views.users, name='users'),
    path('', views.index, name='index'),
    # path('form/', views.form_name_view, name='form_name'),
    path('login', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name="special")
]

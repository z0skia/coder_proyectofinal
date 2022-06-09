from django.urls import path
from blog import *
from .views import *
#USER SISTEM
from django.contrib.auth.views import LogoutView




urlpatterns = [
    #BLOG
    path('', index, name='index'),
    path('blog/', dash, name='dash'),
    path('blog/dash', dash, name='dash'),
    path('about', about, name='about'),
    #CRUD
    path('blog/post/<int:pk>/', post_detail, name='post_detail'),
    path('blog/post/new', new_post, name='new_post'),
    path('blog/post/<int:pk>edit/', edit_post, name= 'edit_post'),
    path('blog/post/<int:pk>delete/', delete_post, name= 'delete_post'),
    #USER SISTEM
    path('login', login_request, name='login'),
    path('register', register, name='register'),
    path('registerok',register, name='registerok'),
    path('logout', LogoutView.as_view(template_name='blog/logout.html'), name='logout')
]



from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('',views.index, name="index" ),
        path('about',views.about, name="about" ),
        path('blog',views.blog, name="blog" ),
        path('contact',views.contact, name="contact" ),
        path('coffee',views.coffee, name="coffee" ),
        path('order/<int:id>',views.order, name="order" ),

        path('signup',views.signup, name="signup" ),
        path('login',views.login, name="login" ),
        path('logout',views.logout, name="logout" ),
]

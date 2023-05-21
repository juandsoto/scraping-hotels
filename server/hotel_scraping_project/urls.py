"""
URL configuration for hotel_scraping_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from user_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # User
    path('create_user/', views.create_user, name='create_user'),
    path('get_users/', views.get_users, name='get_users'),
    path('get_user/<int:user_id>/', views.get_user, name='get_user'),
    path('delete_user/<int:user_id>/', views.modify_user, name='delete_user'),
    #path('modify_user/<int:user_id>/', views.delete_user, name='delete_user'),

    #News
    path('news/', views.NewsList.as_view(), name='NewsList'),
    path('news/<int:news_id>', views.NewsId.as_view(), name='NewsId'),
    path('news/create', views.NewsCreate.as_view(), name='NewsCreate'),
    path('news/delete/<int:news_id>', views.NewsDelete.as_view(), name='NewsDelete'),

]

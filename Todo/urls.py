"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from work.views import Registration,Signin,Add_task,Delete_task,Update,Logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Registration.as_view()),
    path('log/', Signin.as_view(),name='log'),
    path('todo/', Add_task.as_view(),name='todo'),
    path('delete/<int:pk>', Delete_task.as_view(),name='delete'),
    path('update/<int:pk>', Update.as_view(),name='update'),
    path('logout/', Logout_view.as_view(),name='logout'),
]
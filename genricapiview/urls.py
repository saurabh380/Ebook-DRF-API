"""genricapiview URL Configuration

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
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ebook_create.as_view()),
    path('list/',views.ebook_listview.as_view()),
    path('detail/<int:pk>/',views.ebook_detailview.as_view()),
    path('list/<int:ebook_pk>/review/', views.review_create.as_view()),
    path('<int:pk>/', views.review_update.as_view()),


]

"""codingdojo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register, name="register"),
    path('lender_register',views.lender_register,name="lender_register"),
    path('', views.index, name="index"),
	path('lender_login', views.lender_login, name='lender_login'),
	path('borrower_login', views.borrower_login, name='borrower_login'),
	path('lender_register', views.lender_register, name='lender_register'),
	path('borrower_register', views.borrower_register, name='borrower_register'),
	path('borrower_home', views.borrower_home, name='borrower_home'),
	path('lender_home', views.lender_home, name='lender_home'),
	path('lender_logout', views.lender_logout, name='lender_logout'),
	path('borrower_logout', views.borrower_logout, name='borrower_logout'),
	path('borrower/<borrower_id>/lend', views.lend),
	path('borrower/<borrower_id>/delete', views.delete),
	path('borrower_login_page', views.borrower_login_page, name='borrower_login_page'),
	path('lender_login_page', views.lender_login_page, name='lender_login_page'),
]

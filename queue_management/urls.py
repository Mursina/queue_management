"""queue_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from home import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate_token', views.generate_token),
    path('update_counter_status', views.update_counter_status),
    path('check_token_assignment', views.check_token_assignment),
    path('choose_service_mode', views.choose_service_mode),
    path('update_system_configuration', views.update_system_configuration),
    path('authorized', views.authorized),
]

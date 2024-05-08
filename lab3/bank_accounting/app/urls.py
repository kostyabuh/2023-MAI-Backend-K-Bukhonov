"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('accs', views.accs, name='accs'),
    path('acc/<uuid:acc_id>', views.acc, name='acc'),
    path('acc/search', views.search_acc, name='search_acc'),
    path('acc/create', views.create_acc, name='create_acc'),
    path('clients', views.clients, name='clients'),
    path('client/<uuid:client_id>', views.client, name='client'),
    path('client/create', views.create_client, name='create_client'),
    path('workers', views.workers, name='workers'),
    path('worker/<uuid:worker_id>', views.worker, name='worker'),
    path('worker/create', views.create_worker, name='create_worker'),
]

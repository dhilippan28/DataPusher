"""
URL configuration for my_project project.

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
from django.urls import path
from data_pusher import views

urlpatterns = [
    path('account/', views.AccountListView.as_view()),
    path('account/<int:pk>', views.AccountDetailsView.as_view()),
    path('destination/', views.DestinationListView.as_view()),
    path('destination/<int:pk>', views.DestinationDetailsView.as_view()),
    path('account_with_destinations/<int:pk>', views.AccountWithDestinationListView.as_view()),
    path('server/incoming_data', views.IncomingData.as_view()),

]

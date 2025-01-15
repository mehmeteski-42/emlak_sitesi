"""
URL configuration for emlak_sitesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('', views.home, name='home'),
<<<<<<< Updated upstream
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('add-listing/', views.add_listing, name='add_listing'),
=======
    path('arsa/', views.arsa, name='arsa'),  # Arsaların listelendiği sayfa
    path('ev/', views.ev, name='ev'),
    path('tarla/', views.tarla, name='tarla'), # Arsaların listelendiği sayfa

>>>>>>> Stashed changes
]

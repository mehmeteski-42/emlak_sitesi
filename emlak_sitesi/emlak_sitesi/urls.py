# emlak_sitesi/urls.py
from django.contrib import admin
from django.urls import path, include
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),  # API URLs
    path('', views.home, name='home'),
    path('arsa/', views.arsa, name='arsa'),  # Arsaların listelendiği sayfa
    path('ev/', views.ev, name='ev'),  # Arsaların listelendiği sayfa

]

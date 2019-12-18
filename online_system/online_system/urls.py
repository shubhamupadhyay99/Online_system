from product_app import views

from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product_app.urls')),
    url(r'^accounts/', include('allauth.urls')),
]

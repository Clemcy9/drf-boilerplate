from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import Item


router = DefaultRouter()
router.register(r'items',ItemViewSet)

class MyAdminSite(AdminSite):
    site_header = "My Custom Admin"
    site_title = "Admin Portal"
    index_title = "Welcome to My Admin"

my_admin_site = MyAdminSite(name='myadmin')

my_admin_site.register(Item)

urlpatterns = [
    path('', include(router.urls)),
    path('myadmin/', my_admin_site.urls )
]
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import generate_static_sitemap  # Ensure the correct import

sitemaps = {
    'static': generate_static_sitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path("admin/", admin.site.urls),
    path('', include('portfolio.urls')),
]
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['blogs']

    def location(self, item):
        return reverse(item)
    
    # def save(self, obj):
    #     super().save(obj)
    #     # Submit the new URL to Bing Webmasters
    #     submit_to_bing(obj.get_absolute_url())
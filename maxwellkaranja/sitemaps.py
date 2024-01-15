from django.http import HttpResponse
from django.urls import reverse

def generate_static_sitemap(request):
    # List of static URL names
    static_url_names = ['home', 'about', 'contact']

    # Create the root element of the XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Iterate through each static URL
    for url_name in static_url_names:
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{request.build_absolute_uri(reverse(url_name))}</loc>\n'
        xml_content += f'    <changefreq>daily</changefreq>\n'
        xml_content += f'    <priority>0.8</priority>\n'
        xml_content += '  </url>\n'

    # Close the root element
    xml_content += '</urlset>'

    # Return the XML as an HTTP response
    response = HttpResponse(xml_content, content_type='application/xml')
    return response

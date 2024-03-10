import os
import datetime

def generate_sitemap(directory):
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                loc = os.path.join('https://danielmelloo.github.io/CloudHub/', os.path.relpath(os.path.join(root, file), directory))
                lastmod = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root, file))).strftime('%Y-%m-%d')
                sitemap += f'    <url>\n'
                sitemap += f'        <loc>{loc}</loc>\n'
                sitemap += f'        <lastmod>{lastmod}</lastmod>\n'
                sitemap += f'        <changefreq>weekly</changefreq>\n'
                sitemap += f'        <priority>0.8</priority>\n'
                sitemap += f'    </url>\n'

    sitemap += '</urlset>\n'
    return sitemap

if __name__ == "__main__":
    directory = os.getcwd()  # Diretório atual onde o script está localizado
    sitemap_content = generate_sitemap(directory)

    with open('sitemap.xml', 'w') as f:
        f.write(sitemap_content)

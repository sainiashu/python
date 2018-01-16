import requests
import beautifulsoup4

url = 'http://github.com'
r = requests.get(url)
r_html = r.text
soup = beautifulsoup4(r_html)
title = soup.find('span', 'articletitle').string
print(title)



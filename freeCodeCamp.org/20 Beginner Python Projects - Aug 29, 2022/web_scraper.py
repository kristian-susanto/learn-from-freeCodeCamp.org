# pip install requests bs4
import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub User: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')

img_tag = soup.find('img', {'class': 'avatar avatar-user width-full border color-bg-default'})
if img_tag:
    profile_image = img_tag['src']
    print('Profile image URL:', profile_image)
else:
    print('Profile image not found.')
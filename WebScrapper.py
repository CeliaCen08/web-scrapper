from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/Sanrio-Hello-Kitty-Snack-Box/dp/B07VQV7NJY/ref=sr_1_1?crid=3EOJ3JQRCNE3A&dib=eyJ2IjoiMSJ9.jUQPBLOCEG2KHZwhdQyk53gIJg3ajbQHfXFNfVvB3S_jet8M0E8LsSzfc-eUdGSsSC_fyLS-XfNgqFXcZrKnnBF9-7poQCHgaCFtec3I5vO3g54we_R_J1E0tBdaIScNEVOvTM4ISf2vvH-2H1AOM4YaR8Xp2HNhjcU0GEH_INpB1a5jZr2hWvaEzMud0FXol3S-ByvRvA4nfdDk8D4MZ64RjUI3KgjO-OePujufxFxeXWpCzd9piYrMX_DXZt6A60XNg9hz6ZrjXiRyihwZX0hmgoVz7movwck8mYq1_lM.lMkl8Jk7ulNaS0bDx4mZJ6NN18oqrmv9M9peaE7L3d8&dib_tag=se&keywords=sanrio&qid=1719545114&sprefix=sanrio%2Caps%2C74&sr=8-1'
custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9'
}

response = requests.get(url, headers=custom_headers)
soup = BeautifulSoup(response.text, "lxml")  # Ensure lxml is installed

image_element = soup.select_one('#landingImage')
image = image_element.attrs.get('src')

print(image)

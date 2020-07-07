import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# NewEgg GIGABYTE B450M DS3H AM4 AMD B450 SATA 6Gb/s Micro ATX AMD Motherboard
NE_Giga = 'https://www.newegg.com/p/pl?d=GIGABYTE%20B450M%20DS3H&N=8000'

# Opens Website URL & Downloads Page HTML
uClient = uReq(NE_Giga)

# Store Elements into variable
test = uClient.read()

# Close Page Connection
uClient.close()

# HTML parser
parser = soup(test, "html.parser")

# container = parser.find("div", {"class":"wrapper"})
# product_name = container.h1.span.text
#
container = parser.find("div", {"class":"item-info"})
container = container.text[10:]
product_name = container.strip()

container = parser.find("div",{"class":"item-action"})
price_box = container.find("li",{"class":"price-current"})
price = (price_box.strong.text + price_box.sup.text)

shipping_box = parser.find("li",{"class":"price-ship"})
shipping = shipping_box.text
print(shipping)

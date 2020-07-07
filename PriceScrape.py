import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#
# fileName = "products.csv"
# file = open(fileName, "w")
# headers = "Name,Price,Shipping,Available\n"
# file.write(headers)
#
# # NewEgg GIGABYTE B450M DS3H AM4 AMD B450 SATA 6Gb/s Micro ATX AMD Motherboard
# NE_Giga = 'https://www.newegg.com/p/pl?d=GIGABYTE%20B450M%20DS3H&N=8000'
# NE_TM  = 'https://www.newegg.com/p/pl?d=MSI%20B450%20TOMAHAWK%20MAX&N=8000'
# NE_GPM = 'https://www.newegg.com/p/pl?d=MSI%20B450%20Gaming%20Plus%20MAX&N=8000'
#
# urls = []
# urls.append(NE_Giga)
# urls.append(NE_TM)
# urls.append(NE_GPM)
#
#
# for url in urls:
#
#     # Opens Website URL & Downloads Page HTML
#     uClient = uReq(url)
#
#     # Store Elements into variable
#     test = uClient.read()
#
#     # Close Page Connection
#     uClient.close()
#
#     # HTML parser
#     parser = soup(test, "html.parser")
#
#     # Gets the product name
#     container = parser.find("div", {"class":"item-info"})
#     container = container.text[10:]
#     product_name = container.strip()
#
#     # Gets the product price
#     container = parser.find("div",{"class":"item-action"})
#     price_box = container.find("li",{"class":"price-current"})
#     price = (price_box.strong.text + price_box.sup.text)
#
#     # Gets the product shipping
#     shipping_box = parser.find("li",{"class":"price-ship"})
#     shipping = shipping_box.text.strip()
#
#     OOS = parser.find("p",{"class":"item-promo"})
#     if OOS.text == "":
#         availability = "In Stock"
#     else:
#         availability = OOS.text
#
#     file.write(product_name.replace(",","|") + "," + price + "," + shipping + "," + availability + "\n")
#
# file
#
# file.close()


# Opens Website URL & Downloads Page HTML
uClient = uReq('https://www.microcenter.com/search/search_results.aspx?Ntk=all&sortby=match&N=4294966996+4294818892&myStore=true')

# Store Elements into variable
test = uClient.read()

# Close Page Connection
uClient.close()

# HTML parser
parser = soup(test, "html.parser")

# Gets the product name
container = parser.find("ul", {"role": "tabpanel"})
product_list = container.findAll("li")
name_list = []
price_list = []
i = 0
for product in product_list:
    singleProduct = product_list[i].find("a", {"class": "image"})
    name = singleProduct['data-brand'] + " " + singleProduct['data-name']
    name_list.append(name)
    price_list.append(singleProduct['data-price'])
    i += 1

print(price_list)

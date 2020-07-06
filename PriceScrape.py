import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# NewEgg GIGABYTE B450M DS3H AM4 AMD B450 SATA 6Gb/s Micro ATX AMD Motherboard
NE_Giga = 'https://www.newegg.com/gigabyte-b450m-ds3h/p/N82E16813145083?Item=N82E16813145083'

# Opens Website URL & Downloads Page HTML
uClient = uReq(NE_Giga)

# Store Elements into variable
test = uClient.read()

# Close Page Connection
uClient.close()

print(test)
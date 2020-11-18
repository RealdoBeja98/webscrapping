from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import bs4


my_url = 'https://www.newegg.com/p/pl?d=graphics+card'

#opening up connection and grabbing the page
u_client = uReq(my_url)
page_html = u_client.read()
u_client.close()

#html parsing
page_soup = soup(page_html, 'html.parser')


#grabs  each product

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)

containers = page_soup.findAll("div",{"class":"item_container"})
for container in containers:
    brand = container.div.div.a.img["title"]
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class","price-ship"})
    shipping = shipping_container[0].text

    f.write(brand + "," +  product_name.replace(",","|") + "," + shipping + "\n")

f.close()
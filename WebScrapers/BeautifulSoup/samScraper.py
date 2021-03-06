import requests
from bs4 import BeautifulSoup as soup

data = requests.get('https://beta.sam.gov/search?keywords=&sort=-modifiedDate&index=opp&is_active=true&page=1&naics=811213')

#opening up connection, grabbing the page


#Html parsing
soup = soup(data.text, "html.parser")

#grabs each product
print(soup)
#containers = page_soup.findAll("div",{"class":""})

#filename = "products.csv"           # creates .csv file named products
#f = open(filename, "w")             # opens file for input

#headers = "brand, product_name, price, shipping\n"             # table Head dividers

#f.write(headers)

#for container in containers:
    #brand = container.div.div.a.img["title"]                       # finds product brand in an <a> named title

    #title_container = container.findAll("a", {"class":"item-title"})                 #finds product_name in <a>
    #product_name = title_container[0].text

    #price_container = container.findAll("li", {"class":"price-current"})             # finds price in <li>
    #price = price_container[0].text.strip()                                                   # formats to price only

    #shipping_container = container.findAll("li", {"class":"price-ship"})             # finds shipping price in <li>
    #shipping = shipping_container[0].text.strip()                                             # formats to price only

    #print("brand: " + brand)                                                                           # shows results on Console
    #print("product_name: " + product_name)
    #print("price: " + price)
    #print("shipping: " + shipping)

    #f.write(brand + "," + product_name.replace(",", "") + "," + price + "," + shipping + "\n")         #write results to products.csv

#f.close()                  #close file

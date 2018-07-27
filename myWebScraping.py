from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening up the connection and grabbing the page
uClient = uReq(myUrl)

pageHtml = uClient.read()

uClient.close()
#html parsing
pageSoup = soup(pageHtml, 'html.parser')

#grabs each 
containers = pageSoup.findAll('div',{'class':'item-container'})
len(containers)
containers[0]

containers[0].div.div.a.img['title']
fileName = 'products.csv'
f = open(fileName,'w')
headers = 'brand , productName , shipping \n'
f.write(headers)
for container in containers:
	brand = container.div.div.a.img['title']
	titleContainer = container.findAll('a',{'class':'item-title'})
	productName = titleContainer[0].text
	shippingContainer = container.findAll('li',{'class':'price-ship'})
	shipping = shippingContainer[0].text.strip()

	print("brand : " + brand)
	print("productName : " + productName)
	print("shipping : " + shipping)

	f.write(brand +","+ productName.replace(',','|') +','+ shipping + '\n')
f.close()
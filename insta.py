#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import requests
driver = webdriver.Chrome()

#Log into instagram .
#driver.get("http://www.instagram.com/accounts/login")
#driver.sleep(10)
#userName = driver.find_element_by_name('username')
#password = driver.find_element_by_name('password')
#userName.clear()
#userName.send_keys('Ram')
#password.clear()
#password.send_keys('Ram123')
#loginButton = driver.find_element_by_xpath('//form/span/button[text()="Log in"]')
#loginButton.click()

#Search with token and select the first image after search .
token = 'fashion'
driver.get('https://www.instagram.com/explore/tags/'+token)
firstImage = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
firstImage.click()

#Finding the image link and next page link


#Downloading image
imageLink = 'https://instagram.fktm4-1.fna.fbcdn.net/vp/712f4317116593b1d412c194aed88ba5/5C0992E6/t51.2885-15/e35/37866154_240567450116777_351802390418030592_n.jpg'
def saveImage(url):
    r = requests.get(url , stream=True)
    filename = 'image'
    with open(filename , 'wb') as fd:
        for chunk in r.iter_content(chunk_size=10000):
            fd.write(chunk)
saveImage(imageLink)
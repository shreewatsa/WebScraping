#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import requests
driver = webdriver.Chrome()

#Log into instagram .
#def login(username , password):
    #driver.get("http://www.instagram.com/accounts/login")
    #driver.sleep(10)
    #userName = driver.find_element_by_name('username')
    #password = driver.find_element_by_name('password')
    #userName.clear()
    #userName.send_keys('username')
    #password.clear()
    #password.send_keys('password')
    #loginButton = driver.find_element_by_xpath('//form/span/button[text()="Log in"]')
    #loginButton.click()

#Search with token and select the first image after search .
def searchToken(token):
    driver.get('https://www.instagram.com/explore/tags/'+token)
    firstImage = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    firstImage.click()

#Image Download function
def saveImage(url , i):
    r = requests.get(url , stream=True)
    filename = 'image' + str(i)
    with open(filename , 'wb') as fd:
        for chunk in r.iter_content(chunk_size=10000):
            fd.write(chunk)

#Finding the image links
def findAndDownloadLinks():
    i = 0
    imgElems = driver.find_elements_by_tag_name('img')
    for img in imgElems:
        i = i+1
        link = img.get_attribute('src')
        if(link):
            saveImage(img.get_attribute('src'), i)

if __name__ == '__main__':
    token = 'fashion'
    searchToken(token)
    findAndDownloadLinks()

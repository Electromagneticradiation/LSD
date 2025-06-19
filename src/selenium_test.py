from selenium import webdriver                                   # main module of selenium package
from selenium.webdriver.firefox.service import Service           # class to manage lifecycle of browserdriver exe 
from webdriver_manager.firefox import GeckoDriverManager         # class to download/retrieve COMPATIBLE geckodriver

path = GeckoDriverManager().install()
print("\n",path,"\n")
spy = webdriver.Firefox(service=Service(path))

spy.get("https://www.selenium.dev/documentation/")
title = spy.title
i = title.find("Selenium")
print(title[i:i+len("Selenium")])
spy.quit()

from selenium import webdriver                                   # main module of selenium package
from selenium.webdriver.firefox.service import Service           # class to manage lifecycle of browserdriver exe 
from webdriver_manager.firefox import GeckoDriverManager         # class to download/retrieve COMPATIBLE geckodriver

spy = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

spy.get("https://")

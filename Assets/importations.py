from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
from Assets.index import file, popupMessage
from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome = webdriver.Chrome(options=options, executable_path='Assets\chromedriver.exe')
url_site = "http://dmz-5.dmz.org.br:8080/login.jsp?os_destination=%2Fdefault.jsp"
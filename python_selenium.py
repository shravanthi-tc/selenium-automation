#Implementation of Selenium WebDriver with Python using PyTest
 
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver = webdriver.Chrome()

chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
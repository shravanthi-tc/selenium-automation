from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("https://targetclose-test.myshopify.com/admin/apps/jaya-stg")
from selenium import webdriver
# Short cuts insert cell
# Insert cell above A
# Insert cell below B
# Delete cell double click D
# pip (preferred installer program)

time.sleep(5)
driver = webdriver.Firefox()
# driver = webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver_win32.exe")
#driver.maximize_window()
driver.get("https://targetclose-test.myshopify.com/admin/apps/jaya-stg")

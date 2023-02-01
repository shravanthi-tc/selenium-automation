from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# for upload file
from selenium.webdriver.common.action_chains import ActionChains
import autoit
# For select dropdown
from selenium.webdriver.support.select import Select
import time

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

# Try catch block to open partner login
try:
    partner_name = driver.find_elements(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/section/a");
    for value in partner_name:
        print(value.text,"\n")
        if value.text == "Shopify Partners":
            print("success")
            button_click = driver.find_element(By. XPATH  ,"/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/section/a")
            button_click.click()
            break     
except :
    print("An exception occurred")
# Email enter login section

account_email_id = element = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID,"account_email")))
account_email_id.send_keys("shravanthi@targetclose.com");
email_login_button = WebDriverWait(driver, 30).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/form/button")))
email_login_button.click();

time.sleep(5)

# Password enter login section

account_password  = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID,"account_password")))
account_password.send_keys("nandeesh@123");
password_login_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/form/div[2]/ul/button")))
password_login_button.click();

time.sleep(10)
# Switch from shopify store to app iframe
driver.switch_to.frame("app-iframe")
time.sleep(10)

# Click on edit button

edit_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By. XPATH  ,"/html/body/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr[1]/td[6]/button")))
edit_button.click();

# Choose call response mode 

time.sleep(2)
select_call_response= Select(driver.find_element(By.CLASS_NAME,"Polaris-Select__Input")) 

# select call response mode as voice

select_call_response.select_by_index(0)
ActionChains(driver).move_to_element( driver.find_element(By.CLASS_NAME,"Polaris-DropZone__Container")).click().perform()
time.sleep(2)

# File upload from firefox start

 # File upload from firefox end


handle = "[CLASS:#32770; TITLE:File Upload]"
autoit.win_wait(handle, 60)
time.sleep(2)
autoit.control_set_text(handle, "Edit1", r"voice.mp3")
autoit.control_click(handle, "Button1")

time.sleep(2)
save_updates_call_response = driver.find_element(By.XPATH,"//*[@id='AppFrameMain']/div/div/div[2]/div/div/form/div/div/div[2]/div/div[1]/button")
save_updates_call_response.click();


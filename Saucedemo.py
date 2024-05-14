from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from selenium.webdriver.common.by import By

paths = r"C:\Users\dhivy\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")

# Entering username
username_field = driver.find_element(By.ID, "user-name")
username = "standard_user"
username_field.send_keys(username)

# Entering password
password_field = driver.find_element(By.ID, "password")
password = "secret_sauce"
password_field.send_keys(password)

# Clicking the login button
login_button= driver.find_element(By.ID, "login-button")
login_button.click()

driver.maximize_window()

# Extracting the title of the webpage
webpage_title = driver.title
print("Webpage Title:", webpage_title)

# Getting the current URL of the webpage
current_url = driver.current_url
print("Current URL:", current_url)


# Execute JavaScript to get the text content of the body tag
webpage_content = driver.execute_script("return document.body.innerText")

# Print the extracted content
print("Web Page content:",webpage_content)

# Saving the content to a text file
filename = "Webpage_task_11.txt"
#This function call opens the file named filename in write mode ('w') with UTF-8 encoding. Writing in UTF-8 encoding ensures that Unicode characters can be properly encoded and written to the file.
with open(filename, 'w', encoding='utf-8') as file:
  file.write(webpage_content)

driver.quit()

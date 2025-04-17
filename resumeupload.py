from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
from dotenv import load_dotenv

resume_file_path = "C:\\Users\\BHARATH\\Desktop\\HemanthKumarResume.pdf"  # Update this path

load_dotenv()

def login_to_naukri():
    email = os.getenv("NAUKRI_EMAIL")
    password = os.getenv("NAUKRI_PASSWORD")

    driver = webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    sleep(3)

    # Click on the "Login" button (usually top-right)
    login_button = driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()
    sleep(3)

    # Switch to login iframe if needed
    try:
        iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[id*="login-iframe"]')
        driver.switch_to.frame(iframe)
    except:
        pass  # No iframe, continue

    # Now fill in email and password
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your active Email ID / Username"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()

    sleep(5)
    print("✅ Logged into Naukri successfully!")
    driver.switch_to.default_content()
    return driver

# === Close driver ===
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re  

def get_available_data(driver):
    wait = WebDriverWait(driver, 10)

    # The XPath of the element containing available data
    available_data_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="available-assign-data"]')))

    # Extract the numeric part from the text using a regular expression
    available_data_text = available_data_element.text
    match = re.search(r'\d+', available_data_text)
    
    if match:
        available_data = int(match.group())
        return available_data
    else:
        print("Could not extract numeric value from available data text.")
        return None

def assign_data(driver, data):
    wait = WebDriverWait(driver, 30)

    driver.get("http://182.163.99.86/login")

    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys("admin@gigatech.com")
    password_input.send_keys("Abc@123")
    button.click()

    time.sleep(3)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Login successful. URL changed to:", new_url)
    else:
        print("Login failed or URL did not change.")
        return

    time.sleep(5)
    driver.get("http://182.163.99.86/dashboard/projects")

    time.sleep(5)
    driver.get("http://182.163.99.86/dashboard/projects/364")
    time.sleep(5)

    driver.get("http://182.163.99.86/dashboard/projects/364/group/91")
    time.sleep(8)

    data_button = driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]')
    data_button.click()

    wait = WebDriverWait(driver, 10)

    data_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section/div/input')))
    data_input.send_keys(data)

    time.sleep(3)

    available_data = get_available_data(driver)

    if available_data is not None and int(data) <= available_data:
        assign_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')

        if assign_button.is_enabled():
            assign_button.click()
            print("TEST PASSED: Data is assigned successfully.")
        else:
            print("TEST PASSED: Assign Data button is not clickable with the provided data.")
    else:
        print("TEST PASSED: Input value is greater than available data.")

# Test Case 1: Invalid data
driver = webdriver.Chrome()
assign_data(driver, '0')
print("Assign data failed")
driver.quit()

# Test Case 2: Input value greater than available data
driver = webdriver.Chrome()
assign_data(driver, '200')
print("Input value greater than available data. Assign data failed")
driver.quit()

# Test Case 3: Valid data
driver = webdriver.Chrome()
assign_data(driver, '5')
print("Data assigned successfully")
driver.quit()



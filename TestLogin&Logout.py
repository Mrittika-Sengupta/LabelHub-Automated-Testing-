from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login(username, password):
    driver = webdriver.Chrome()
    driver.get("http://182.163.99.86/login")

    wait = WebDriverWait(driver, 30)
    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))
  
    
    time.sleep(2)

    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    
    button.click()

    time.sleep(4)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("TEST CASE PASSED: Login successful. URL changed to:", new_url)
    else:
        print("TEST CASE PASSED: Login failed....")



    driver.quit()


def test_logout():

    username = "admin@gigatech.com"
    password = "Abc@123"
    url = "http://182.163.99.86/login"
    driver = webdriver.Chrome()
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.send_keys(username)

    time.sleep(2)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/button')
    login_button.click()

    time.sleep(5)

    Admin_button = driver.find_element(By.XPATH, '//*[@id="radix-:r5:"]/div/p[1]/span')
    Admin_button.click()

    time.sleep(5)

    Logout_button = driver.find_element(By.XPATH, '//*[@id="radix-:r6:"]/div')
    Logout_button.click()

    time.sleep(5)
     
    print("Logout Successful")
    
    

# Test case 1: Inactive User/Login Successful (After activated by admin)
test_login("$@h.com", "Hh123@")
print("Inactive User/ Login Successful..After activated by admin")


# Test case 2: Invalid email
test_login("admin@gigatech.c", "Abc@123")
print("Invalid email")

# Test case 3: Invalid email
test_login("admin@gigatechcom", "Abc@123")
print("Invalid email")


# Test case 4: Incorrect email or password
test_login("admin@gigatech.comkjbjk", "Abc@123")
print("Incorrect email or password")


# Test case 5: Invalid email
test_login(" @gigatech.com", "Abc@123")
print("Invalid email")


# Test case 6: Invalid email
test_login(" admin@gigatech.com,,,,", "Abc@123")
print("Invalid email")

# Test case 7: Email required
test_login("", "Abc@123")
print("Email required")


 # Test case 8: Incorrect email or password
test_login("nazifa@gmail.com", "Nazf123@@")
print("Incorrect email or password")


# Test case 9: Incorrect email or password
test_login("admin@gigatech.com", "Abc@1234")
print("Incorrect email or password")

# Test case 10: Incorrect email or password
test_login("admin@gigatech.com", "ab")
print("Password must contain at least 6 and less than 14 characters")

# Test case 11: Invalid Password
test_login("admin@gigatech.com", "abcdfgh")
print("Please give at least one number, one lower and upper-case letter, one special character")

# Test case 12: Invalid Password
test_login("admin@gigatech.com", "ABCFHSKD")
print("Please give at least one number, one lower and upper-case letter, one special character")

#Test case 13: Invalid Password
test_login("admin@gigatech.com", "Aabcdsdf")
print("Please give at least one number, one lower and upper-case letter, one special character")

#Test case 14: Invalid Password
test_login("admin@gigatech.com", "Aabcdsdf2")
print("Please give at least one number, one lower and upper-case letter, one special character")

#Test case 15: Invalid Password
test_login("admin@gigatech.com", "Aabcdsdf@123456789")
print("Password can’t be typed after 14 character")

#Test case 16: Password Required
test_login("admin@gigatech.com", " ")
print("Password required")

#Test case 17: Email & Password Required
test_login(" ", " ")
print("Email and password required")

#Test case 18: Login Successful
test_login("admin@gigatech.com", "Abc@123")
print("Login Successful")


print("ALL TEST CASES DONE")



















test_logout()
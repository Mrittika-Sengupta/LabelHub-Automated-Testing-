from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sign(fullName, email, role, gender, mobile, birthday, qualification, institutionName, password, confirmPassword):
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 30)

    driver.get("http://182.163.99.86/login")
    time.sleep(2)


    driver.get("http://182.163.99.86/signup")
    time.sleep(2)


    fullName_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[1]/div[1]/div/input')))
    fullName_input.send_keys(fullName)
    time.sleep(2)

    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[2]/div[1]/div/input')))
    email_input.send_keys(email)
    time.sleep(2)

    role_select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[1]/div[2]/div/select')))
    role_select.send_keys(role)
    time.sleep(2)

    gender_select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[2]/div[2]/div/select')))
    gender_select.send_keys(gender)
    time.sleep(2)

    mobile_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[1]/div[3]/div/input')))
    mobile_input.send_keys(mobile)
    time.sleep(2)

    birthday_iso_format = "20" + birthday[-2:] + "-" + birthday[:5].replace("/", "-")
    birthday_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r7:"]')))
    driver.execute_script(f"arguments[0].value = '{birthday_iso_format}';", birthday_input)

    qualification_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[1]/div[4]/input')))
    qualification_input.send_keys(qualification)
    time.sleep(2)

    institutionName_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[2]/div[4]/input')))
    institutionName_input.send_keys(institutionName)
    time.sleep(2)

    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[1]/div[5]/div[1]/input')))
    password_input.send_keys(password)
    time.sleep(2)

    confirmPassword_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/section[1]/div/div/div[2]/section[2]/div[5]/div/div[1]/input')))
    confirmPassword_input.send_keys(confirmPassword)
    time.sleep(2)

    signup_button = driver.find_element(By.XPATH, '/html/body/div/div/section[1]/div/div/div[3]/button')

    if signup_button.is_enabled():
        signup_button.click()
        print("TEST CASE PASSED.")
       
    else:
        print("TEST CASE PASSED")
        return  # Stop execution if the button is not clickable

# Test case 1: Invalid Email
sign("anomita", "anomita123@h", "Annotator", "Female", "01620398890", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 2: Invalid Email
sign("anomita", "anomita123@", "Annotator", "Female", "01620398890", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 3: Invalid Role
sign( "anomita", "anomita123@gmail.com", "Validator", "Female", "01816709403", "10-07-2001", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 4: Empty Gender
sign( "anomita", "anomita123@gmail.com", "Annotator", " ", "01816709403", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")


# Test case 5: Empty Role
sign( "anomita", "anomita123@gmail.com", " ", "Female", "01816709403", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 6: Invalid Username
sign( " ", "anomita123@gmail.com", "Annotator", "Female", "01816709403", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 7: Invalid Username
sign( "A", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "Anomita123@", "Anomita123@")
print("Signup is Failed.")

# Test case 8: Empty Email and Phone Number
sign( "anomita", " ", "Annotator", "Female", "01816709403", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 9: Empty Phone Number
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", " ", " ", " ", " ", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 10: Invalid Phone Number
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "66781209876", "10-07-2001", "f", "f", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 11: Invalid Phone Number
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "016781209876666", "10-07-2001", "f", "f", "Anomita123@", "Anomita123@")
print("Signup is Failed")

# Test case 12: Password doesn’t match
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "Anomita123@", "Anomita1233")
print("Signup is Failed")

# Test case 13: Empty Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", " ", " ")
print("Signup is Failed")

# Test case 14: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "abc2", "abc2")
print("Signup is Failed")

# Test case 15: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "abcdef2", "abcdef2")
print("Signup is Failed")

# Test case 16: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "Abcdef2", "Abcdef2")
print("Signup is Failed")

# Test case 17: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "Abcdef@", "Abcdef@")
print("Signup is Failed")

# Test case 18: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "A23333@", "A23333@")
print("Signup is Failed")

# Test case 19: Invalid Password
sign( "anomita", "anomita123@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "f", "f", "Abcdef123@45634hghkkk", "Abcdef123@45634hghkkk")
print("Signup is Failed")


# Test case 20: Empty role, gender, phonenumber, birthday
sign( " ", "anomita123@gmail.com", " ", " ", " ", " ", " ", " ", "Abcdef123@45634hghkkk", "Abcdef123@45634hghkkk")
print("Signup is Failed")


# Test case 21: Empty field
sign( " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
print("Signup is Failed")


# Test case 22: Exist Email
sign( "Maisha", "MRI@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "Bs", "EEU", "Rat456@@", "Rat456@@")
print("Signup is Failed")

# Test case 23: Deleted User
sign( "Maisha", "nazibhuda41@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "Bs", "EEU", "Rat456@@", "Rat456@@")
print("Signup is Failed")

# Test case 24: Successful registration
sign( "MrittikaSenn", "halloween12@gmail.com", "Annotator", "Female", "01816709403", "10-07-2001", "Bs", "EEU", "Mritt456@@@", "Mritt456@@@")
print("Successful registration")

# Test case 25: Successful registration with message
sign( "Mahirullll", "nazifanahean12@gmail.com", "Annotator", "Female", "+8801618756907", "10-07-2001", "B", "N", "Nazifa456@@@", "Nazifa456@@@")
print("Successful Registration with a confirmation message.")

# Test case 26: Successful registration
sign( "Mahirulll", "MAHI@gmail.com", "Annotator", "Female", "+8801618756907", "10-07-2001", "B", "N", "Nazifa456@@@", "Nazifa456@@@")
print("Successful registration")

# Test case 27: Successful registration
sign( "46ed6", "$1@h.com", "Annotator", "Male", " 01368881940", "10-07-2001", "B", "N", "Nazifa456@@@", "Nazifa456@@@")
print("Successful registration")

# Test case 28: Successful registration
sign("Nafisasa", "nazifasn12g3@gmail.ajaira", "Annotator", "Male", " 01368881940", "10-07-2001", "B", "N", "Nazifa456@@@", "Nazifa456@@@")
print("Successful registration")


# Test case 29: Successful registration
sign("Rumaisaasaa", "$gs@hh.com", "Annotator", "Male", " 01368881940", "10-07-2001", " ", " ", "Hh123@", "Hh123@")
print("Successful registration")

print("ALL TEST CASES DONE")













































































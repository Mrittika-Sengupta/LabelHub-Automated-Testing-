from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def add_user(full_name, email, gender, dob, institution_name, qualification, password, mobile, role):
    
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
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


 

    time.sleep(5)
    driver.get("http://182.163.99.86/users")
    time.sleep(5)



    time.sleep(5)
    add_user_button = driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/button')
    add_user_button.click()

    full_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[1]/input')))
    full_name_input.send_keys(full_name)

    time.sleep(5)

    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[1]/input')))
    email_input.send_keys(email)

    time.sleep(5)

    gender_select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[2]/select')))
    gender_select.send_keys(gender)

    time.sleep(5)

    # Format the birthday input
    birthday_iso_format = "20" + dob[-2:] + "-" + dob[:5].replace("/", "-")
    birthday_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[2]/input')))
    driver.execute_script(f"arguments[0].value = '{birthday_iso_format}';", birthday_input)

    time.sleep(5)

    institution_name_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[3]/input')))
    institution_name_input.send_keys(institution_name)

    time.sleep(5)

    qualification_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[3]/input')))
    qualification_input.send_keys(qualification)

    time.sleep(5)

    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[4]/input')))
    password_input.send_keys(password)

    time.sleep(5)

    mobile_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div[4]/input')))
    mobile_input.send_keys(mobile)

    time.sleep(5)

    role_select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/div[5]/select')))
    role_select.send_keys(role)

    time.sleep(5)

    add_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')

    if add_button.is_enabled():
        add_button.click()
        print("Test Cases Passed")
    else:
        print("Test Cases Passed")

# Test Case 1: valid details 
add_user( "Naihann", "naihanunanj1122@gmail.com", "Female", "02-01-2002", "BRC", "MS", "Naha123@", "01718258042", "Manager")
print("Successfully added")

# Test Case 2: valid details 
add_user("Kamrrull", "kh99112300@gmail.com", "Male", "02-07-2002", "BRC", "MS", "Amin456@", "01718258042", "Annotator")
print("Successfully added")

# Test Case 3: valid details 
add_user("Nazifaaa", "nazifaaaa.nahian@northsouth.edu", "Female", "05-01-2002", "BRC", "MS", "Atia123@", "01718258042", "Validator")
print("Successfully added")

# Test Case 4: valid details 
add_user("Tahminaaaa", "taaahminakhatoonn456@gmail.com", "Female", "05-01-2002", "BRC", "MS", "Asha456@", "01718258042", "Guest")
print("Successfully added")


# Test Case 5: Enter Invalid and Non-Existing email address
add_user("bulbulllll", "%@h.ccccccc", "Male", "02-07-2002", "BRC", "MS", "Asha456@", "01718258042", "Guest")
print("Successfully added")



# Test Case 6: field empty
add_user(" ", "nafisatasfiya123@gmail.com", " ", "05-01-2002", " ", " ", "Asha456@", " ", "Guest")
print("Please fill out name, email, phone & password")

# Test Case 7: field empty
add_user("Nafisa", " ", " ", "05-01-2002", " ", " ", "Asha456@", "01718258042", "Guest")
print("Add button does not work")

# Test Case 8: field empty
add_user("Nafisa", "nafisatasfiya123@gmail.com", " ", "05-01-2002", " ", " ", "Asha456@", " ", "Guest")
print("Add button does not work")

# Test Case 9: field empty
add_user("Nafisa", "nafisatasfiya123@gmail.com", " ", "05-01-2002", " ", " ", "Asha456@", "01718258042", "Guest")
print("Please fill out name, email, phone & password")

#Test Case 10:Keeping “Role” field empty
add_user("Nafisa", "nafisatasfiya123@gmail.com", "Female", "05-01-2002", "ABC", "SSC", "Asha456@", "01718258042", " ")
print("Successfully added as guest role")

#Test Case 11: Role required
add_user("Nafisa", "nafisatasfiya123@gmail.com", " ", " ", " ", " ", "Asha456@", "01718258042", " ")
print("Successfully added as guest role")

#Test Case 12: Successfully added as guest role
add_user(" Tasfiya", "nafisatasfiya123@gmail.com", "Female", "07-27-2000", " ", " ", "Asha456@", "01718258042", "Validator")
print("Successfully added as guest role")

#Test Case 13: Enter already registered mail by user
add_user(" Tasfiya", "halloween12@gmail.com", "Female", "07-27-2000", " ", " ", "Asha456@", "01718258042", "Validator")
print("An user with this email already exists")

#Test Case 14: Enter already registered mail by user
add_user(" Tasfiya", "nazibhuda41@gmail.com", "Female", "07-27-2000", " ", " ", "Asha456@", "01718258042", "Validator")
print("An user with this email already exists")

#Test Case 15: Enter the mail of Admin
add_user(" Admin2", "admin@gigatech.com", "Female", "07-27-2000", " ", " ", "Asha456@", "01718258042", "Validator")
print("An user with this email already exists")

#Test Case 16: Enter an Invalid Name
add_user("$$4", "sephora567@yahoo.com", "Female", " ", " ", " ", "Asha456@", "01718258042", "Validator")
print("An user with this email already exists")

#Test Case 17: Enter an Invalid Name
add_user("Ilma", "seph@yahoo.com", "Female", " ", " ", " ", "Asha456@", "8888888", "Validator")
print("Please enter a valid phone number")

#Test Case 18: Enter an Invalid Name
add_user("Ilma", "seph@yahoo.com", "Female", " ", " ", " ", "Asha456@", "01718678905666", "Validator")
print("Please enter a valid phone number")

#Test Case 19:valid Mobile Number with country code
add_user("Ilma", "ilma@yahoo.com", "Female", " ", " ", " ", "Asha456@", "+8801712025702", "Validator")
print("Successfully added")


#Test Case 20 Enter wrong format password
add_user("Ilma", "luna@yahoo.com", "Female", " ", " ", " ", "asha", "+8801712025702", "Validator")
print("Password must contain at least 6 and at most 14 characters, at least one number, one lower case, one upper case letter and a one special character.")

#Test Case 21 Enter wrong format password
add_user("Ilma", "luna@yahoo.com", "Female", " ", " ", " ", "ashaaa12", "+8801712025702", "Validator")
print("Password must contain at least 6 and at most 14 characters, at least one number, one lower case, one upper case letter and a one special character.")

#Test Case 22 Enter wrong format password
add_user("Ilma", "luna@yahoo.com", "Female", " ", " ", " ", "Asha@@", "+8801712025702", "Validator")
print("Password must contain at least 6 and at most 14 characters, at least one number, one lower case, one upper case letter and a one special character.")

#Test Case 23 Enter wrong format password
add_user("Ilma", "luna@yahoo.com", "Female", " ", " ", " ", "ASHA@@", "+8801712025702", "Validator")
print("Password must contain at least 6 and at most 14 characters, at least one number, one lower case, one upper case letter and a one special character.")

#Test Case 24 Enter wrong format password
add_user("Ilma", "luna@yahoo.com", "Female", " ", " ", " ", "Addddddd123@dddddddd", "+8801712025702", "Validator")
print("Password must contain at least 6 and at most 14 characters, at least one number, one lower case, one upper case letter and a one special character.")

#Test Case 25 All Empty Field
add_user(" ", " ", " ", " ", " ", " ", " ", " ", "  ")
print("Add does not work")

print("ALL TEST CASES DONE")

















































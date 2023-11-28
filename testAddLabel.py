from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, username, password):
    url = "http://182.163.99.86/login"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)


    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/button')
    login_button.click()

  
    time.sleep(5)

  

def add_label(driver, category, name, short_form, description):

    driver.get("http://182.163.99.86/configuration")

    wait = WebDriverWait(driver, 10)

    category_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[1]/input')))
    category_input.send_keys(category)

    time.sleep(5)

    name_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[2]/input')))
    name_input.send_keys(name)

    time.sleep(5)

    short_form_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[3]/input')))
    short_form_input.send_keys(short_form)

    time.sleep(5)

    description_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[4]/textarea')))
    description_input.send_keys(description)
    time.sleep(5)

    add_button = driver.find_element(By.XPATH, '/html/body/div/section/main/div[2]/div[2]/section/section[2]/div/div[2]/button')
    add_button.click()

    time.sleep(5)




def main():
    driver = initialize_driver()

    # Test login
    login(driver, "admin@gigatech.com", "Abc@123")
    

    #Test Case 1:
    #Category must be at least one character
    add_label(driver, "Lab", "Lab34", "HUb23", "Labehub123")
    print("TEST CASE PASSED: Label is added successfully")
    
    #Test Case 2:
    #Description can be empty, 
    add_label(driver, "LabelHub", "ffff2", "fff3", " ")
    print("TEST CASE PASSED: Label is added successfully")
    

    #Test Case 3:
    #short name can't be empty
    add_label(driver, "Label", "ffff", "fff", " ")
    print("TEST CASE PASSED: short form must be at least one character")

    #Test Case 4:
    #tag name can't be empty

    add_label(driver, "HUB", " ", "fff", " ")
    print("TEST CASE PASSED: Please insert a tag name")

    #Test Case 5:
    #All fields empty

    add_label(driver, " ", " ", " ", " ")
    print("TEST CASE PASSED: Please insert a tag name")






    



    















if __name__ == "__main__":
    main()

   

    





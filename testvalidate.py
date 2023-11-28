from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

###### validate with edit 
def validateEdit(action):
    
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 30)


    driver.get("http://182.163.99.86/login")

    number = action

    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))

    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys("mahirulxbox1@gmail.com")
    password_input.send_keys("Nsu123?")
    button.click()

    time.sleep(3)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Login successful. URL changed to:", new_url)
    else:
        print("Login failed or URL did not change.")

        ### moves to project page and annotation page 
        time.sleep(5)

    driver.get("http://182.163.99.86/projects")

    time.sleep(5)
    driver.get("http://182.163.99.86/projects/231")
    time.sleep(5)

    driver.get("http://182.163.99.86/projects/231/group/55/ongoing")
    time.sleep(8)

    
    if number == 1: 
        ###edit button
        # Find the element by its XPath
        edit = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[2]")

        # Click on the element
        edit.click()
        time.sleep(8)

        label_selector = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[1]/div/div/div/div[2]/div/span")
        label_selector.click()
        time.sleep(5)
        word_index=2
        #xpath = f"//span[@data-i='{word_index}']"
        xpath = "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[1]/span[4]"
        time.sleep(3)

        elements = driver.find_elements(By.XPATH, xpath)


        if not elements:
            driver.quit()
            print("Word does not exist")
        else:
            print("Word Found")

            text_selector = driver.find_element(By.XPATH, xpath)
            
            action = ActionChains(driver) ## Action chains object must be called with driver as parameter to call double_click function (imported on line 5)
            action.double_click(text_selector).perform()
            time.sleep(5)
            #####################################################

            action = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]")
            time.sleep(5)
            action_button = action
            action_button.click()
            print("Submit Button Pressed")
            print("Test Passed: Annotation is validated and submitted")

            time.sleep(3)

    elif number==2:
            edit = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[2]")
            time.sleep(3)
            edit.click()
            time.sleep(3)

            action = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[2]")
            time.sleep(5)
            action_button = action
            action_button.click()
            print("Reject Button Pressed")
            print("Test Passed: Annotation is rejected")
            time.sleep(3)

    elif number==3:
            edit = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[2]")
            edit.click()
            time.sleep(3)

            action = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]")
            time.sleep(5)
            action_button = action
            action_button.click()
            time.sleep(3)
            print("Submit Button Pressed without changes")
            print("Test  Passed: Annotation is validated- no changes made")
    
    else: 
            print("Button Not Pressed, Test Case did not pass")

    print("TESTING DONE")
    driver.quit()    

###### validate with Like  

def validateLike():
     
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 30)

    driver.get("http://182.163.99.86/login")

    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))

    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys("mahirulxbox1@gmail.com")
    password_input.send_keys("Nsu123?")
    button.click()

    time.sleep(3)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Login successful. URL changed to:", new_url)
    else:
        print("Login failed or URL did not change.")

        ### moves to project page and annotation page 
        time.sleep(5)

    driver.get("http://182.163.99.86/projects")

    time.sleep(5)
    driver.get("http://182.163.99.86/projects/231")
    time.sleep(5)

    driver.get("http://182.163.99.86/projects/231/group/55/ongoing")
    time.sleep(8)     

    like_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/section/div[2]/div/div[1]/div/div[1]/button")
    time.sleep(2)
    like_button.click()
    time.sleep(4)
    print("Annotation Submitted through LIKE button")
    print("TEST PASSED: Annotation Validted and submitted through LIKE BUTTON")
    driver.quit()    


#TEST CASE 1: Annotation submitted: Edit button pressed, and text is labelled
validateEdit(1)
print("TEST CASE 1 DONE")
##TEST CASE 2: Reject button pressed, no change made to the text
validateEdit(2)
print("TEST CASE 2 DONE")
#TEST CASE 3: Annotation submitted: Submit button pressed with no changes made to the text
validateEdit(3)
print("TEST CASE 3 DONE")
#TEST CASE 4: Annotation submitted: Like button pressed
validateLike()
print("TEST CASE 4 DONE")
print("All Test Cases Completed")

















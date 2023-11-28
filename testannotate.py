from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def annotate(label, word_index, action):
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 30)
    driver.maximize_window()
    number = action

    driver.get("http://182.163.99.86/login")

    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))

    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys("labelhub_annotator@northsouth.edu")
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
    driver.get("http://182.163.99.86/projects/364")
    time.sleep(5)

    driver.get("http://182.163.99.86/projects/364/annotation/91")
    time.sleep(8)

    ############### Submit, Reject, Skip button
    if number == 1:  # if submit is pressed after annotating
        ################################## annotates with label only if submit is chosen as parameter 
        label_selector = driver.find_element(By.XPATH, label)  # label
        label_selector.click()
        time.sleep(8)

        ### Construct the XPath to find the <span> element with the specified `data-i` attribute value

        xpath = f"//span[@data-i='{word_index}']" ##each bangla word has  a data-i value which increases per word here 12 means word number 12 is selected
        ### data_i_value = word_index 
        elements = driver.find_elements(By.XPATH, xpath)

        if elements:
            # finds this Xpath and adds to text_selector variable
            # Find the <span> element by XPath
            text_selector = driver.find_element(By.XPATH, xpath)
            # text_selector is passed as parameter for double_click function to double click bangla text, here data-i value 12 will be selected. data-i value can be checked from inspect 
            # Use ActionChains to perform a double-click on the element
            action = ActionChains(driver) # Action chains object must be called with driver as parameter to call double_click function (imported on line 5)
            action.double_click(text_selector).perform()
            time.sleep(5)

            action = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]")
            time.sleep(3)
            action_button = action
            action_button.click()
            print("TEST PASSED: Submit Button Pressed")
            time.sleep(3)
        else:
            print("TEST PASSED: Word does not exist")

    elif number == 2:  # if skip is passed
        action = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/footer/button[2]")
        time.sleep(3)
        action_button = action
        action_button.click()
        print("TEST PASSED: Skip Button Pressed")
        time.sleep(5)
        
        ## After skipped, it will go to the skipped dashboad
        driver.get(f"http://182.163.99.86/projects/364/annotation/91/skipped")
        time.sleep(8)
        #Annote the the Skipped sentence and update 
        annotate_button = driver.find_element(By.XPATH, "//button[text()='Annotate']")
        annotate_button.click()
        time.sleep(8)
        ##Select Label
        label_selector = driver.find_element(By.XPATH, label)  # label
        label_selector.click()
        time.sleep(8)

        xpath = f"//span[@data-i='{word_index}']"
        elements = driver.find_elements(By.XPATH, xpath)

        if elements:
            text_selector = driver.find_element(By.XPATH, xpath)
            action_update = ActionChains(driver)
            action_update.double_click(text_selector).perform()
            time.sleep(8)

            action = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]")
            time.sleep(8)
            action_button = action
            action_button.click()
            print("TEST PASSED: Submit Button Pressed after updating")
            time.sleep(8)
             
             ##It will go the ongoing dashboard, and also edit the annotation
            driver.get(f"http://182.163.99.86/projects/364/annotation/91/ongoing")
            time.sleep(8)

            edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
            edit_button.click()
            time.sleep(8)

            action = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/section[2]/div/div/div[2]/button[1]")
            time.sleep(8)
            action_button = action
            action_button.click()
            print("TEST PASSED: Submit Button Pressed after Editing")
            time.sleep(8)

        else:
            print("TEST PASSED: Word does not exist")

    elif number == 3:  # if reject is passed
        action = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div/section[3]/div/div/footer/button[3]")
        time.sleep(8)
        action_button = action
        action_button.click()
        print("TEST PASSED: Reject Button Pressed")
        time.sleep(8)

    elif number == 4:  # if submit is passed without annotating
        action = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div/section[3]/div/div/footer/button[1]")
        time.sleep(8)
        action_button = action
        action_button.click()
        print("TEST PASSED: Submit Button Pressed without annotating")
        time.sleep(8)
    else:
        print("TEST PASSED: Button Not Pressed, Test Case did not pass")

   

    driver.quit()


### label 
#### Noun
event = "//span[text()='EVENT']"
per = "//span[text()='PER']"
loc = "//span[text()='LOC']"
unit = "//span[text()='UNIT']"
num = "//span[text()='NUM']"
dt = "//span[text()='D&T']"
tt = "//span[text()='T&T']"
org = "//span[text()='ORG']"
per = "//span[text()='PER']"

### Actions:
 # 1 = submit 
 # 2 = skip 
 # 3 = reject
 # 4 = submit without annotating


# TEST CASE 1: Annotate and Submit
annotate(per, 2, 1)
# TEST CASE 2: Skip
annotate(per, 2, 2)
# TEST CASE 3: No Annotation and Submit
annotate(per, 2, 4)
# TEST CASE 4: Word Index out of bounds
annotate(per, 100, 1)
# TEST CASE 5: Reject
annotate(per, 2, 3)

print("ALL TEST CASES DONE")
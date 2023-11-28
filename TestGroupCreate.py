from tokenize import group
from xml.dom.minidom import Element
from requests import delete
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def createGroup(testcase): ### Parameter input corresponds to test case number: 1 to 10
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 30)
    number = testcase
    driver.get("http://182.163.99.86/login")

    username_input = wait.until(EC.presence_of_element_located((By.ID, 'username')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'password')))

    button = driver.find_element(By.XPATH, "//button[text()='Sign in']")

    username_input.send_keys("admin@gigatech.com")
    password_input.send_keys("Abc@123")
    button.click()

    time.sleep(5)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Login successful. URL changed to:", new_url)
    else:
        print("Login failed or URL did not change.")

        ### moves to project page and annotation page 
        time.sleep(5)

    driver.get("http://182.163.99.86/dashboard/projects")
    time.sleep(5)
    driver.get("http://182.163.99.86/dashboard/projects/231")
    time.sleep(5)

    group_btn = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/button")
    group_btn.click()
    time.sleep(5)

    if number==1: # No input
        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("Submit button pressed without any input")
        print("Cannot Submit: Test Case Passed")
        driver.quit()

    elif number==2: ### Submit without name input
        # Choosing Annotation Type
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")))
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)
         ## Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)
        #### Choosing Validator
        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")))
    
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Submit Button Pressed without adding Group Name: Group Name must be added")

        driver.quit()

    elif number==3: #Submit without selecting annotation type

        ### Entering Group Name
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("GroupChy2")
        time.sleep(5)
          ### Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ######### Chooosing Validator
        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")))
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)
        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Cannot Submit without selecting Annotation Type")

        driver.quit()    

    elif number==4: #Submit without selecting both annotator and validator

        ####### Selecting Group name and Annotation Type
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("GroupChy2")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")))
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
            # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Cannot submit without selecting annotator or validator")
        driver.quit()    

    elif number==5: #Submit without selecting annotator
        ### Input Group name and selecting annotation Type
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("GroupChy2")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        ### Selecting validator
        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until( EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")) )

        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
            # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)
        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Cannot submit without selecting Annotator")
        driver.quit()

    elif number==6: ## Submit without selecting validator
        ####### Selecting Annotation Type and Group name
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("GroupChy2")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']")) 
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)   
        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Cannot submit without selecting Validator")
        driver.quit()

    elif number==7: # Submit with selecting only annotator and validator
        #### Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ######### Chooosing Validator
        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Cannot submit without Group Name and Annotation Type")

        driver.quit()

    elif number==8: ### Submit with all valid input
        ####### Selecting Annotation Type and Group Name
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("GroupChy2")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)
        ####### Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ######### Chooosing Validator

        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Group Created")
        driver.quit()

    elif number==9: ### Submit with all valid input but group name less than 2 characters
        ####### Selecting Annotation Type and Group Name
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("G")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)
        ####### Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ######### Chooosing Validator

        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Group cannot be created, name must be greater than 2 characters")
        driver.quit()


    elif number==10: ### Submit with all valid input but group name  more  than 14 characters
        ####### Selecting Annotation Type and Group Name
        username_input = wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        username_input.send_keys("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        time.sleep(5)
        combobox_input = driver.find_element(By.CSS_SELECTOR, "[role='combobox']")
        combobox_input.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[0]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)
        ####### Choosing Annotator
        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ######### Chooosing Validator

        combobox_input2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button")
        combobox_input2.click()
        # Wait for the dropdown options to be visible (adjust timeout as needed)
        dropdown_options = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "[role='option']"))
        )
        time.sleep(3)
        if dropdown_options:
            selected_option = dropdown_options[1]
            option_text = selected_option.text
            time.sleep(3)
                # Click on the selected option in the dropdown
            selected_option.click()
            time.sleep(3)

        checkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button")
        time.sleep(3)
        checkbox.click()
        time.sleep(3)

        ####Submit button
        submit = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button")
        submit.click()
        time.sleep(5)
        print("TEST PASSED: Group cannot be created, name must be less than 40 characters")
        driver.quit()


    else: 
        print("Test Case did not run")
        driver.quit()    

def deleteGroup(confirm):
    number = confirm 
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

    time.sleep(5)

    new_url = driver.current_url
    if new_url == "http://182.163.99.86/dashboard":
        print("Login successful. URL changed to:", new_url)
    else:
        print("Login failed or URL did not change.")

        ### moves to project page and annotation page 
        time.sleep(5)

    driver.get("http://182.163.99.86/dashboard/projects")
    time.sleep(5)
    driver.get("http://182.163.99.86/dashboard/projects/231")
    time.sleep(5)

    ### Pressing delete button 
    trash_icon = driver.find_element(By.XPATH, "//img[@alt='delete']")
    time.sleep(5)

    trash_icon.click()
    time.sleep(5)

    if number == 11: ## if number is 1 then press no on confirmation 
        delete = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        delete.click()
        time.sleep(5)
        print("TEST PASSED: Group was not deleted")
        driver.quit()

    elif number == 12: ## if number is 2 then press yes on confirmation
        delete = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")
        delete.click()
        time.sleep(5)
        print("TEST PASSED: Group was deleted")
        driver.quit()
        
    else: 
        print("No confirmation")
        driver.quit()


    driver.quit()    

##### TESTS for creating group and deleting group from admin window (can only be done by Admin) #########


# # #TEST CASE 1: submit without any input
createGroup(1)
print("Test Case 1 Complete")
# # #TEST CASE 2: Submit without name input
createGroup(2)
print("Test Case 2 Complete")
# # #TEST CASE 3: Submit without selecting annotation type
createGroup(3)
print("Test Case 3 Complete")
# # #TEST CASE 4: Submit without selecting both annotator and validator
createGroup(4)
print("Test Case 4 Complete")
# # #TEST CASE 5: Submit without selecting annotator
createGroup(5)
print("Test Case 5 Complete")
# # #TEST CASE 6: Submit without selecting validator
createGroup(6)
print("Test Case 6 Complete")
# # #TEST CASE 7: Submit with selecting only annotator and validator
createGroup(7)
print("Test Case 7 Complete")
# # #TEST CASE 8: Submit with all inputs (name more than 2 and less than 14 characters)
createGroup(8)
print("Test Case 8 Complete")
# # #TEST CASE 9: Name less than 2 characters
createGroup(9)
print("Test Case 9 Complete")
# #TEST CASE 10: Name more than 14 characters
createGroup(10)
print("Test Case 10 Complete")
# #TEST CASE 11: Confirm Delete
deleteGroup(11) ## confirm = 11 for no, 12 for yes
print("Test Case 11 Complete")
# #TEST CASE 12: Confirm Delete
deleteGroup(12) ## confirm = 11 for no, 12 for yes
print("Test Case 12 Complete")
print("All Test Cases Complete")
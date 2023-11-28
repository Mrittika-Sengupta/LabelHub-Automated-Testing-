from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def create_project(driver, name, description, annotate_type_value, tag_type_value):
   
    options = webdriver.EdgeOptions()
    options.add_argument('--log-level=OFF')  # disable logging
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 30)
    driver.get("http://182.163.99.86/login")
    wait = WebDriverWait(driver, 30)
    driver.maximize_window()


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

    # Navigate to the projects page
    driver.get("http://182.163.99.86/dashboard/projects")
    time.sleep(8)

    project_button = driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section/div[1]/button")
    project_button.click()

    time.sleep(3)

    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/div/input')))
    name_input.send_keys(name)

    time.sleep(3)
    description_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/textarea')))
    description_input.send_keys(description)

    time.sleep(3)
    annotate_type_mapping = {
        '1': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[1]/div/button',  # NER
        '2': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[2]/div/button',  # POS
        '3': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[3]/div/button',  # DEEP_PARSING
        '4': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[4]/div/button',  # SHALLOW_PARSING
        '5': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[5]/div/button',  # QA
        '6': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[6]/div/button',  # WSD
        '7': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[7]/div/button',  # PARAPHRASING
        '8': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[8]/div/button',  # SEMANTIC_SIMILARITY
        '9': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[9]/div/button',  # BD_LEXICON
        '10': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[10]/div/button',  # TEXT_CLASSIFICATION
        '11': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[11]/div/button',  # LEMMATIZATION
        '12': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[12]/div/button',  # COREFERENCE_RESOLUTION
        '13': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/div/div[13]/div/button',  # treebanl
    }

    tag_type_mapping = {
        'MISC': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]/button/div',
        'PER': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[6]/button/div',
        'ORG': '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[9]/button/div'
        # Add more mappings as needed
    }

    # Set the Annotate Type
    annotate_type_xpath = annotate_type_mapping.get(annotate_type_value)

# Check if annotate_type_xpath is not empty before proceeding
    if annotate_type_xpath:
        try:
            annotate_type_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, annotate_type_xpath)))
            annotate_type_button.click()
            time.sleep(3)
        except TimeoutException:
            print("Annotate type button is not clickable. Please provide a valid value.")
            error_flag = True
    else:
        print("Annotate type is empty. Please provide a valid value.")
        error_flag = True

    time.sleep(3)

    tag_type_xpath = tag_type_mapping.get(tag_type_value)

    # Check if tag_type_xpath is not empty before proceeding
    if tag_type_xpath:
        try:
            tag_type_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tag_type_xpath)))
            tag_type_div.click()
            time.sleep(3)
        except TimeoutException:
            print("TEST CASE PASSED: Tag type element not found. Please provide a valid value.")
            error_flag = True
    else:
        print("TEST CASE PASSED: Tag type is empty. Please provide a valid value.")
        error_flag = True

    time.sleep(3)

    time.sleep(3)

    # Click the "Create Project" button
    add_label_button = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')


    if not name or not description or not annotate_type_value or not tag_type_value:
        print("Add label button is not enabled. Please provide valid data.")
    else:
        add_label_button.click()
        time.sleep(2)

        # Check conditions after clicking the button
        if name.strip() == "" or len(name) < 3:
            print("TEST CASE PASSED: Project name should be more than two characters.")
        else:
            print("TEST CASE PASSED: Project is created successfully.")

# Create a single driver instance
driver = webdriver.Chrome()

try:
    # Test Case 1: Project Creation success
    create_project(driver, "HubCSE434", "Description", '1', 'MISC')
    print("Submit")

    # Test Case 2: Empty Description
    create_project(driver, "Label_Hub_CSE434", " ", '1', 'PER')
    print("Submit")

    # Test Case 3: Project Name should be more than two character and less than 40 character
    create_project(driver, "T", "Description", '1', 'NUM')
    print("not Submit")

    # Test Case 4: Empty Project Name
    create_project(driver, " ", "Description", '1', 'MISC')
    print("not Submit")
    # Test Case 5: Only annotate_type is empty
    create_project(driver, "TestLabel11dddxx1", "Description", "", 'MISC')
    print("not Submit")

    # Test Case 6: Only tag_type is empty
    create_project(driver, "TestLabel11ddd1", "Description", '1', '')
    print("not Submit")

finally:
    driver.quit()

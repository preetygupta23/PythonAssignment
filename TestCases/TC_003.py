from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Base import InitiateDriver

def test_VerifyTourBooksTab():
    driver = InitiateDriver.startbrowser() #Initiating the driver and Opening the URL
    driver.find_element_by_id("manage-btn").click()  #Clicking on Map Marker tab
    wait = WebDriverWait(driver,20)
    driver.switch_to.window(driver.window_handles[1]) #waiting until new window is opened
    wait.until(expected_conditions.new_window_is_opened) #Switching to child window
    assert driver.current_url == "https://tours.propertycapsule.com/" #Verifying the title of child window



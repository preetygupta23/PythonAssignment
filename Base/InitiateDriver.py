from selenium.webdriver import Firefox

# Initiating the Driver
def startbrowser():
    global driver
    path = "./Driver/geckodriver.exe" #Picking the driver from driver folder
    driver = Firefox(executable_path=path)
    driver.get("https://www.propertycapsule.com") #Opening the URL
    driver.maximize_window()  #Maximizing the window
    yield
    driver.close()  #Clsoing the driver

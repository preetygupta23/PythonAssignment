from Base import InitiateDriver


def test_ValidateHomePage():
    driver = InitiateDriver.startbrowser()  #Initiating the driver and Opening the URL
    assert driver.find_element_by_xpath("//img[@src='assets/images/pcVTSGreyLogo.png']").text == "Property Capsule + VTS" #verifying the logo


from selenium.webdriver.common.by import By

class LoginLocators:
    LOGO = By.XPATH, "//div[@id='divLogo']//img"
    USERNAME = By.ID, "txtUsername"
    PASSWORD = By.ID, "txtPassword"
    LOGIN_BUTTON = By.ID, "btnLogin"
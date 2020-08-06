from behave import *
from selenium import webdriver
from locators.login import LoginLocators

@given(u'launch chrome browser')
def launchBrowser(context):
    #context.driver= webdriver.Chrome(executable_path="C:\src\python\selenium\drivers\chromedriver.exe")
    context.driver = webdriver.Chrome()


@when(u'open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that the logo present on the page')
def verifyLogo(context):
    status = context.driver.find_element(*LoginLocators.LOGO).is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
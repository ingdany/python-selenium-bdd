from behave import *
from selenium import webdriver
from locators.login import LoginLocators
from locators.dashboard import DashboardLocators

@given(u'I launch to Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when(u'I open orange HRM Homepage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(*LoginLocators.USERNAME).send_keys(user)
    context.driver.find_element(*LoginLocators.PASSWORD).send_keys(pwd)


@when(u'Click in login button')
def step_impl(context):
    context.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()


@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(*DashboardLocators.DASHBOARD_LABEL).text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
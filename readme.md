# Python-Selenium-BDD
Example using Python Selenium with Behave Package

## Install Behave (Cucumber)
`pip install behave`

## Develop Feature
`$ behave features/orangehrm.feature`

## Create Steps
Copy scenario definitions to your steps file

```
@given(u'launch chrome browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given launch chrome browser')


@when(u'open orange hrm homepage')
def step_impl(context):
def step_impl(context):
    raise NotImplementedError(u'STEP: Given launch chrome browser')


@when(u'open orange hrm homepage')
def step_impl(context):
    raise NotImplementedError(u'STEP: When open orange hrm homepage')


@then(u'verify that the logo present on the page')


@then(u'verify that the logo present on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify that the logo present on the page')


@then(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')
```

## Execute
`$ behave features/orangehrm.feature`

## Allure Report with Behave

You need to have previously installed Allure

1. Install Allure Behave Package
`$ pip install allure-behave`

2. Create reports folder

3. To run your behave and return a behave report
`behave -f allure_behave.formatter:AllureFormatter -o reports/ features`

4. To see your report you need to run allure server
`allure serve reports/`
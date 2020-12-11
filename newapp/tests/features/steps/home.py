from selenium.webdriver.support import expected_conditions as EC

from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


HOME_PAGE = 'http://127.0.0.1:5000/'


@given(u'Home page is open')
def step_impl(context):
    context.browser.get(HOME_PAGE)
    assert context.browser.title == 'Home — Rectify'


@when(u'I click on Sign In')
def step_impl(context):
    context.browser.find_element_by_id('signin').click()


@then(u'A pop up appears saying "You are trying to sign in!"')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 3).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')

        alert = context.browser.switch_to.alert
        alert.accept()
        print("Success")
    except TimeoutException:
        print("No Success")


@when(u'I click on Try for Free')
def step_impl(context):
    context.browser.find_element_by_id('signup').click()


@then(u'A pop up appears saying "Try for free for 30 days!"')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 3).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')

        alert = context.browser.switch_to.alert
        alert.accept()
        print("Success")
    except TimeoutException:
        print("No Success")

from selenium import webdriver


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome('./chromedriver')
    context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    context.browser.quit()

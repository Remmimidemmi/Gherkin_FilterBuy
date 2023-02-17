import time

from behave import fixture, use_fixture

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def browser(context):
    print("Browser init")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(5)
    context.browser = browser
    context.browser.maximize_window()
    yield context.browser
    time.sleep(2)
    context.browser.quit()


def before_feature(context, arg):
    # use the same browser instance for all scenarios in the feature
    # if you want to run fresh browser session on each scenario put it in before_scenario()
    use_fixture(browser, context)

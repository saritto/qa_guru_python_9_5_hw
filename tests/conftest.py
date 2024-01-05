import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_zoom = '50%'

    yield

    browser.quit()

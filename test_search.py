import pytest
from selene import browser, be, have


@pytest.fixture
def browser_settings():
    browser.config.window_width = 800
    browser.config.window_height = 600
    browser.open('https://duckduckgo.com')


def test_search(browser_settings):
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('qa.guru - Курсы тестировщиков'))

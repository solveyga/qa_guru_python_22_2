from selene import browser, be, have

def test_search():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    browser.element('html').should(have.text('qa.guru - Курсы тестировщиков'))

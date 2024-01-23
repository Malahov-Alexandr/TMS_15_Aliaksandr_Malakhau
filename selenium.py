def test_example(browser):
    browser.get("https://www.google.com")
    assert "Example Domain" in browser.title

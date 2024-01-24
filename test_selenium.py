def test_example(driver):
    browser.get("https://www.google.com")
    assert "Example Domain" in browser.title

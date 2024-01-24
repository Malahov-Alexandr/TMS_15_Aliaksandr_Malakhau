def test_example(driver):
    driver.get("https://www.google.com")
    assert "Example Domain" in driver.title

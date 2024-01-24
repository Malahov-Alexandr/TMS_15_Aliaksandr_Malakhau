def test_example(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

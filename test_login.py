from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
wait = WebDriverWait(driver, 10)

# Test 1: Invalid credentials
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("invalidUser")
driver.find_element(By.ID, "password").send_keys("wrongPass")
driver.find_element(By.ID, "submit").click()
error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
assert "Your username is invalid!" in error.text, "Error message not shown"
print("Test 1 PASSED: Invalid credentials error displayed")

# Test 2: Valid credentials
driver.get("https://practicetestautomation.com/practice-test-login/")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
success = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".post-title")))
assert "Logged In Successfully" in success.text, "Login failed"
print("Test 2 PASSED: Login successful")

driver.quit()

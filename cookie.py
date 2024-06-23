from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get("https://youtube.com")

cookie = {
    "name": "SOCS",
    "value": "CAESEwgDEgk0ODE3Nzk3MjQaAmVuIAEaBgiA_LyaBg",
    "domain": "youtube.com",  # Replace with the actual domain
    "path": "/",  # Path for which the cookie is valid
    "expiry": int(time.time()) + 3600  # Set cookie to expire in 1 hour
}

driver.add_cookie(cookie)

driver.get("https://youtube.com")

while True:
    time.sleep(1)
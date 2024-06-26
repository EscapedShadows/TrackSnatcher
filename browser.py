def main():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    import re

    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Edge(options=options)
    driver.get("https://youtube.com")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-spec-button-shape-next.yt-spec-button-shape-next--filled.yt-spec-button-shape-next--mono.yt-spec-button-shape-next--size-m'))
    )
    
    button.click()

    links = []
    old = ""

    while True:
        current = driver.current_url

        if current == old:
            pass
        else:
            old = current
            links.append(current)

        if current == "http://exit.com/":
            break

        sleep(.1)

    print(links)

    watch_links = []

    for link in links:
        if re.match(r'https://www\.youtube\.com/watch\?v=.*', link):
            watch_links.append(link)

        if re.match(r'https://www\.youtube\.com/shorts/.*', link):
            watch_links.append(link)

    watch_links = list(set(watch_links))

    driver.quit()

    return watch_links
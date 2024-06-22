from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pywinauto import application
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
import time
import requests

def scrape_trending_topics(mail, userid, password, scraper_api_key):
    # Function to set up ScraperAPI proxy
    def get_scraperapi_url(url):
        return f'http://api.scraperapi.com?api_key={scraper_api_key}&url={url}'

    # Function to get current IP address
    def get_current_ip():
        response = requests.get(get_scraperapi_url('http://httpbin.org/ip'))
        return response.json()['origin']

    # Get the current IP address
    current_ip = get_current_ip()

    # Set up Chrome options to use ScraperAPI proxy
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={get_scraperapi_url("")}')

    # Connecting to chrome and redirect to X login page using ScraperAPI proxy
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(get_scraperapi_url("https://x.com/"))
    time.sleep(3)

    # Click on the button sign in
    sign_in = driver.find_element(By.XPATH, ('//a[@href="/login"]'))
    driver.execute_script("arguments[0].scrollIntoView(true);", sign_in)
    sign_in.click()
    time.sleep(3)

    # Bring the chrome window to foreground to make the buttons clickable
    app = application.Application().connect(title_re=".*Chrome.*")
    chrome_window = app.top_window()
    chrome_window.set_focus()

    time.sleep(3)

    # Click on the email element
    email_element = driver.find_element(By.XPATH, ('//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7"]'))
    email_element.click()
    email_element.send_keys(mail + Keys.ENTER)

    time.sleep(3)

    # Handle possible verifying window
    chrome_window.set_focus()
    heading = driver.find_element(By.XPATH, ('//h1'))
    inner_HTML = heading.text

    if(inner_HTML == "Enter your phone number or username"):
        chrome_window.set_focus()
        username = driver.find_element(By.XPATH, ('//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7" and @type="text"]'))
        username.click()
        username.send_keys(userid + Keys.ENTER)
        time.sleep(3)

    chrome_window.set_focus()
    password_element = driver.find_element(By.XPATH, ('//input[@class="r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7" and @type="password"]'))
    password_element.click()
    password_element.send_keys(password + Keys.ENTER)
    time.sleep(3)

    # Handle the welcome to x.com popup
    try:
        x_popup = driver.find_element(By.XPATH, '//span[text()="Welcome to x.com!"]')
        innerText = x_popup.text
        if innerText == "Welcome to x.com!":
            cross = driver.find_element(By.XPATH, '//button[@class="css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l"]')
            cross.click()
    except NoSuchElementException:
        pass

    chrome_window.set_focus()

    # Function to find and click an element
    def find_and_click(xpath):
        for _ in range(5):
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                try:
                    element.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", element)
                return
            except (StaleElementReferenceException, TimeoutException):
                time.sleep(1)
        raise Exception("Element not found or is constantly stale")

    find_and_click('//a[@href="/explore/tabs/for-you"]')
    time.sleep(3)

    chrome_window.set_focus()
    trending_button = driver.find_element(By.XPATH, '//span[@class="css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3" and text()="Trending"]')
    trending_button.click()
    time.sleep(3)

    Trends = []
    for i in range(5):
        trending_topics = driver.find_element(By.XPATH, f'(//div[@class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e"])[{i+1}]')
        Trends.append(trending_topics.text)

    driver.quit()

    print(f"IP Address used: {current_ip}")
    print(Trends)
    print("Scraped top 5 trending topics")
    
    return current_ip, Trends

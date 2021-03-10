from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.reddit.com")
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.youtube.com")
browser.find_element_by_id('search').send_keys('pesquisar')
time.sleep(5)
browser.switch_to_window(browser.window_handles[0])
browser.find_element_by_id('header-search-bar').send_keys('pesquisar')
time.sleep(10)
browser.get("https://python.org")

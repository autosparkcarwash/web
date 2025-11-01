# AutoSpark Mockup Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, os

def capture(url, output, width, height):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument(f'--window-size={width},{height}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot(output)
    driver.quit()

if __name__ == '__main__':
    os.makedirs('preview', exist_ok=True)
    url = 'http://localhost:8080/index.html'
    capture(url, 'preview/desktop_view.png', 1920, 1080)
    capture(url, 'preview/mobile_view_iphone.png', 430, 932)
    capture(url, 'preview/mobile_view_generic.png', 480, 960)
    print('✅ Mockups generated in /preview folder.')

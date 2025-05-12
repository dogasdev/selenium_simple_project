import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

driver_path = os.path.abspath('./common/chromedriver.exe')
service_system = Service(executable_path=driver_path) #precisa ser um path porque é o caminho até o arquivo executável 
                                                      # que o Selenium vai usar para controlar o navegador.
#Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized") # Roda em segundo plano
chrome_options.add_argument('--lang=pt')

browser = webdriver.Chrome(service=service_system, options=chrome_options)

browser.get('https://github.com/login')
time.sleep(3)


username_input = browser.find_element(By.ID, 'login_field')
password_input = browser.find_element(By.ID, 'password')
login_button = browser.find_element(By.NAME, 'commit')

load_dotenv()
username = os.getenv('GITHUB_USERNAME')
password = os.getenv('GITHUB_PASSWORD')

username_input.send_keys(username)
password_input.send_keys(password)

login_button.click()
time.sleep(5)

def scroll_page():
    for _ in range(30):
        browser.execute_script('window.scrollBy(0, 100);')
        time.sleep(2)

last_height = browser.execute_script('return document.body.scrollHeight')

scroll_page()

tutorial_project_section = browser.find_elements(By.CSS_SELECTOR, 'a.Link.d-flex.flex-column')
print('\nAprenda com Tutoriais:\n')
for tutorial in tutorial_project_section:
    title = tutorial.find_element(By.CLASS_NAME, 'color-fg-accent.text-bold').text
    description = tutorial.find_element(By.CSS_SELECTOR, '.color-fg-muted').text
    print(f"Título: {title}")
    print(f"Descrição: {description}")

browser.quit() 
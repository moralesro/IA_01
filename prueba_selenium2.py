from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Configuración de Selenium
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument('--disable-blink-features=AutomationControlled') 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://openai.com")

sleep(5)

#ver solo el primer titulo
texto = driver.find_element(By.CSS_SELECTOR, "h2").text
print(texto)



#ver todos los titulos h2
titulos = driver.find_elements(By.CSS_SELECTOR, "h2")
for t in titulos:
    print(t.text)

driver.quit()
  
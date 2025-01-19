from selenium import webdriver
from selenium.webdriver.common.by import By

# Configuração do driver
driver = webdriver.Chrome()  # Certifique-se de ter o ChromeDriver instalado
driver.get("https://example.com")

# Exemplo: Capturar texto de um elemento
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)

driver.quit()
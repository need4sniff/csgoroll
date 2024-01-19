from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cesta k vašemu ChromeDriver
# Selenium Grid Hub URL
HUB_URL = 'http://chrome:4444/wd/hub'

# Nekonečná smyčka pro pravidelné aktualizace
while True:
    # Vytvoření instance prohlížeče
    browser = webdriver.Remote(
    command_executor=HUB_URL,
    desired_capabilities=DesiredCapabilities.CHROME
)

    # Otevření stránky
    browser.get('https://www.csgoroll.com/en/roll')

    # Vytvoření instance WebDriverWait
    wait = WebDriverWait(browser, 10)  # Čekání až 10 sekund

    try:
        # Nalezení elementu a získání jeho textu
        element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/cw-root/mat-sidenav-container/mat-sidenav-content/div/cw-roulette/div/header/cw-roulette-game-rolls/section/article/div[3]/span[2]')))
        hodnota = element.text
        print(hodnota)

        # Uložení hodnoty do souboru data.txt
        with open("data.txt", "w") as file:
            file.write(hodnota)
    except Exception as e:
        print("Nepodařilo se najít element: ", e)
    finally:
        # Zavření prohlížeče
        browser.quit()

    time.sleep(20)

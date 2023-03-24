from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

code = input("Geoguessr Game Code: ")

def join_game():
    number = 0
    while number < 10:
        options = Options()
        #options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://geoguessr.com/join")
        # Wait for the page to load
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        game = driver.find_element(By.NAME, "inputBox0")
        game.send_keys(code[0])
        game = driver.find_element(By.NAME, "inputBox1")
        game.send_keys(code[1])
        game = driver.find_element(By.NAME, "inputBox2")
        game.send_keys(code[2])
        game = driver.find_element(By.NAME, "inputBox3")
        game.send_keys(code[3])
        game.send_keys(Keys.RETURN)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "guest-login_content__fdfc2")))
        game = driver.find_element(By.NAME, "nick")
        game.send_keys("AMOGUS")
        game.send_keys(Keys.RETURN)
        number += 1

if __name__ == "__main__":
    join_game()
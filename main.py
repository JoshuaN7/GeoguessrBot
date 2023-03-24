from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

code = input("Geoguessr Game Code: ")

def join_game():
    options = Options()
    #options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://geoguessr.com/join")
    # Wait for the page to load
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    box1 = driver.find_element(By.NAME, "inputBox0")
    box2 = driver.find_element(By.NAME, "inputBox1")
    box3 = driver.find_element(By.NAME, "inputBox2")
    box4 = driver.find_element(By.NAME, "inputBox3")
    box1.send_keys(code[0])
    box2.send_keys(code[1])
    box3.send_keys(code[2])
    box4.send_keys(code[3])
    box4.send_keys(Keys.RETURN)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "guest-login_content__fdfc2")))
    nick = driver.find_element(By.NAME, "nick")
    nick.send_keys("AMOGUS")
    nick.send_keys(Keys.RETURN)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "guess-map guess-map--size-2 guess-map--active guess-map--hidden")))
    map = driver.find_element(By.CLASS_NAME, "guess-map guess-map--size-2 guess-map--active guess-map--hidden")
    map.click()

if __name__ == "__main__":
    join_game()
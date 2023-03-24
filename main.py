from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import names

code = input("Geoguessr Game Code: ")

def join_game():
    options = Options()
    #options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://geoguessr.com/join")
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
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
    nick.send_keys(names.get_first_name())
    nick.send_keys(Keys.RETURN)
    element = wait.until(EC.presence_of_element_located((By.ID, "__next")))
    print("Joined Game")
    url = driver.current_url.split("/") # Split the url to get the game id
    print(url[3])
    response = webdriver.request('POST', 'https://game-server.geoguessr.com/api/duels/'+url[6]+'/pin', data={"lat": "46.78880563216002", "lng": "7.096812793406184", "roundNumber": "1"})
    

if __name__ == "__main__":
    join_game()
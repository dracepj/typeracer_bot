from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class TypeRacer:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.NavigateToRace()
        self.raceText = self.GetText()
        self.Type(self.raceText)
        self.driver.refresh()

    def NavigateToRace(self):
        self.driver.get("https://play.typeracer.com/")
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Enter a typing race"))
            )
            element.click()
        finally:
            print("done")

    def GetText(self):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inputPanel"))
            )
            print(element.text)
            return element.text
        except Exception:
            print("Error: ", Exception)

    def Type(self, text):
        char_array = list(text)
        inputElement = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "txtInput"))
        )
        for item in char_array:
            inputElement.send_keys(item)
            print(item)


#TEST
test = TypeRacer()

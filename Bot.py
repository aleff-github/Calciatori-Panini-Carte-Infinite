from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from random import *
import string

def chrome(chromedriver):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    service_chrome = Service(chromedriver)
    driver = webdriver.Chrome(service=service_chrome)
    driver.get("https://digitalcollection.mypanini.com/")
    return driver

def genera_codice():
    codice = ""
    i = 0
    while True:
        while i < 3: # Codice
            j = 0
            while j < 4:
                lettera_o_numero = randint(0,1)
                if lettera_o_numero == 0:
                    lower_upper_alphabet = string.ascii_letters
                    letter = choice(lower_upper_alphabet)
                    if letter.islower():
                        letter = letter.upper()
                    codice += letter
                else:
                    numero = randint(1,9)
                    codice += str(numero)
                j += 1
            if i != 2:
                codice += "-"
            i += 1
        codici_usati = open("codici_usati.txt", "r").read()
        if codice in codici_usati:
            codice = ""
        else:
            break

    return codice

def segna_nuovo_codice(codice):
    codici_usati = open("codici_usati.txt", "a")
    codici_usati.write("\n" + codice)
    codici_usati.close()

def bot(driver):
    while True:
        codice = genera_codice()

        driver.find_element(By.XPATH, "//*[@id=\"bodyBg\"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/input").send_keys(codice)
        sleep(1)
        driver.find_element(By.XPATH, "//*[@id=\"bodyBg\"]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/button").click()
        sleep(1)
        result = driver.find_element(By.XPATH, "//*[@id=\"text_h4\"]").text
        sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id=\"popup-btn\"]").click()
        sleep(1)
        segna_nuovo_codice(codice)
        print(codice + " - " + result)
    pass

def main():
	# Example of chromedriver path in linux "/home/ale/Documenti/Calciatori Panini/chromedriver"
	# Example of chromedriver path in Windows "C:\\User\Ale\Documenti\Calciatori Panini\chromedriver.exe"
	chromedriver = input("Insert chromedriver path: "
	driver = chrome(chromedriver)
	input("\nLogin and open the dashboard of your album(where you insert the code), then click Send button ")
	bot(driver)
	print("\nEnd.")
main()

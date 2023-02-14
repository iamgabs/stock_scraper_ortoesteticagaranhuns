import json
from time import sleep
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from LoginErrorException import LoginErrorException
from openpyxl.utils.exceptions import InvalidFileException
from readxl import get_matrix_of_products

CREDENTIALS_PATH = 'C:\\Users\\conta\\OneDrive\\Documentos\\scarperdeestoqueortoestetica\\keys.json'

def read_credentials() -> object: 
    credentials_array = []
    try:
        with open(CREDENTIALS_PATH, 'r', encoding='utf-8') as credentials:
            login_keys = json.load(credentials)
            for key, value in login_keys.items():
                if key != '' and value != '':
                    credentials_array.append(value)
                else:
                    raise LoginErrorException
            return credentials_array
    except:
        raise LoginErrorException('An error occourred while reading the login credentials, please check it before!')


try:
    browser = webdriver.Edge()
    browser.get('https://sistema.clinicorp.com/login/')

    get_credentials = read_credentials()

    sleep(1)
    # get email's input 
    email = browser.find_element(By.ID, 'username')
    email.send_keys(get_credentials[0], Keys.RETURN)
    sleep(1)

    # get password's input 
    password = browser.find_element(By.ID, 'password')
    password.send_keys(get_credentials[1], Keys.RETURN)
    sleep(1)

    # login 
    login_button = browser.find_element(By.TAG_NAME, 'span')
    login_button.click()
    sleep(5)

    # access page by menu 
    browser.find_element(By.XPATH, '//*[@id="header__left-container"]/div[1]/button').click()
    sleep(1)

    # click - 'estoque button' 
    browser.find_element(By.XPATH, '//*[@id="navigation_drawer_nav_itens_container"]/div[5]/li/div/button').click()
    sleep(1)

    # #click - 'adicionar produto button'
    browser.find_element(By.XPATH, '//*[@id="show_screen_div"]/div/div/div[1]/div[2]/button').click()
    sleep(10) 



except LoginErrorException: 
    raise LoginErrorException('An error occourred while logging the system!')
except InvalidFileException:
    raise InvalidFileException('An error occourred while reading the file!')
        

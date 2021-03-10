from json import load
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import random



Navegador = webdriver.Chrome(ChromeDriverManager().install())

month=[
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro']

Navegador.get('https://www.instagram.com/accounts/emailsignup/')
Navegador.execute_script("window.open()")
sleep(3)
Navegador.find_element_by_name('emailOrPhone').send_keys((load(open('./dependencias.json'))['telefone']))
Navegador.find_element_by_name('fullName').send_keys('Oliveira Silva')
Navegador.find_element_by_name('username').click()
sleep(1)
Navegador.find_element_by_xpath("//div[@id='react-root']/section/main/div/div/div/div/form/div[5]/div/div/div/button/span").click()
Navegador.find_element_by_name('password').send_keys('Shaman@2584')
Navegador.find_element_by_css_selector('.bkEs3:nth-child(1) > .sqdOP').click()
sleep(2)
Navegador.find_element_by_css_selector('.O15Fw:nth-child(1) > .h144Z').send_keys(month[random.randint(0,11)])
Navegador.find_element_by_css_selector('.O15Fw:nth-child(2) > .h144Z').send_keys(random.randint(1,28))
Navegador.find_element_by_css_selector('.O15Fw:nth-child(3) > .h144Z').send_keys(random.randint(1940,2002))
Navegador.find_element_by_xpath("(//button[@type='button'])[2]").click()
Navegador.switch_to_window(Navegador.window_handles[1])
Navegador.get('https://messages.google.com/web/authentication?hl=pt-BR')
sleep(10)
Navegador.find_element_by_xpath("//span[contains(.,'29091')]").click()
sleep(20)
codSms= Navegador.find_element_by_xpath('//mws-message-wrapper[25]/div/div/div/mws-message-part-router/mws-text-message-part/div/div/mws-message-part-content/div/div')
CodSMSTXT = codSms.text[4:11].replace(' ','')
sleep(2)
Navegador.switch_to_window(Navegador.window_handles[0])
Navegador.find_element_by_name('confirmationCode').send_keys(CodSMSTXT)
sleep(1)
Navegador.find_element_by_xpath("//button[@type='button']").click()

from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
driver.get('http://borg:qa@sosour.pythonanywhere.com/')

driver.maximize_window()

for i in range(10,101):
    input = driver.find_element_by_id('number')
    input.send_keys(i)
    button = driver.find_element_by_id('getFactorial')
    button.click()
    time.sleep(2)
    result = driver.find_element_by_xpath('//*[@id="resultDiv"]')
    result_nr = result.text
    terminate = result_nr.index(': ') + 2
    number = float(result_nr[terminate:])
    input.clear()
    mathfac = float(math.factorial(i))
    print(type(mathfac))
    if mathfac == float(number):
        print("for",i,mathfac,"=",number)
    else:
        print("for",i,mathfac,"=/=",number)

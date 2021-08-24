from selenium import webdriver
import math
import time

driver = webdriver.Chrome()
driver.get('http://borg:qa@sosour.pythonanywhere.com/')

driver.maximize_window()

for i in range(10,101):
    input = driver.find_element_by_id('number') # Finds the input box
    input.send_keys(i) # Inputs the current number in the loop

    button = driver.find_element_by_id('getFactorial') # Finds the "Calculate" button
    button.click() # Clicks the button

    time.sleep(2) # 2 second wait so that results are displayed properly

    result = driver.find_element_by_xpath('//*[@id="resultDiv"]') # Finds the result HTML paragraph
    result_nr = result.text # Extracts the text from the HTML paragraph
    terminate = result_nr.index(': ') + 2
    # Finds the ":" character in the string and counts two characters to the right to only trim the number
    # part of the string
    number = float(result_nr[terminate:]) # Casting the string (with only the number) to a float with scientific notation
    input.clear() # Clears the input box
    mathfac = float(math.factorial(i)) # Calculates the factorial using the math python module, used for comparisons
    if mathfac == float(number): # checks if the python-calculated factorial is the same as the one output by the website
        print("for",i,mathfac,"=",number, "Good")
    else:
        print("for",i,mathfac,"=/=",number, "Bad")

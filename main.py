from words import words
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from config import username, password, autologin
import time
import sys

words_dict = {}

def list_to_dict(words):
    words_dict = {}
    for w in range(len(words)):
        if w % 2 == 0:
            words_dict[words[w]] = words[w+1]
    print(words_dict)
    return words_dict

#url = input('Вставьте URL на тест: ')

test_type = int(input('Выберите тип теста (1 - правописание, 2 - заучивание): '))

url = 'https://quizlet.com/'
#url = 'https://quizlet.com/533038055/learn'
unit_id = input('Вставьте ID юнита из URL: ')
url += unit_id

browser = Firefox()

if autologin == True:
    browser.get("https://quizlet.com/login")
    time.sleep(5)
    username_area = browser.find_element_by_id('username')
    username_area.send_keys(username)
    time.sleep(3)
    password_area = browser.find_element_by_id('password')
    password_area.send_keys(password)
    login_button = browser.find_element_by_xpath('//div[@class="UILoadingButton"]')
    login_button.click()
    time.sleep(10)


browser.get(url)
page = browser.page_source
time.sleep(5)
words = browser.find_elements_by_xpath('//a[@class="SetPageTerm-wordText"]/span')
print(len(words))
words = [el.text for el in browser.find_elements_by_xpath('//div[@class="SetPageTerm-sideContent"]/a/span')]
print(words)
print(list_to_dict(words))
time.sleep(30)

def spelling():
    questions = browser.find_elements_by_xpath('//div[@class="UIDiv SpellQuestionView-inputPrompt--plain"]')
    continue_marks = browser.find_elements_by_xpath('//h2[@class="UIHeading UIHeading--two"]/span')

    if len(questions) > 0:
        answer = words_dict[questions[0].text]
        answer_area = browser.find_element_by_xpath('//textarea[@class="AutoExpandTextarea-textarea"]')
        answer_area.send_keys(answer)
        # Печатаем ответ
        answer_area.send_keys(Keys.RETURN)
        # Нажимаем ENTER
    elif len(continue_marks) > 0:
        #body = browser.find_element_by_xpath('//body')
        #body.send_keys(Keys.RETURN)
        time.sleep(10)
    else:
        sys.exit(0)

def memorization(url):
    

    questions = browser.find_elements_by_xpath('//div[@class="FormattedText notranslate lang-en"]/div')
    continue_marks = browser.find_elements_by_xpath('//h3[@class="UIHeading UIHeading--three"]')

    if len(questions) > 0:
        answer = words_dict[questions[0].text]
        answer_area = browser.find_element_by_xpath('//textarea[@class="AutoExpandTextarea-textarea"]')
        answer_area.send_keys(answer)
        # Печатаем ответ
        answer_area.send_keys(Keys.RETURN)
        # Нажимаем ENTER
    elif len(continue_marks) > 0:
        #continue_marks[0].send_keys(Keys.RETURN)
        #body = browser.find_element_by_xpath('//body')
        #body.send_keys(Keys.RETURN)
        time.sleep(15)
    else:
        sys.exit(0)
if test_type == 1:
    browser.get(url + "/spell")
elif test_type == 2:
    browser.get(url + "/learn")

while True:
    if test_type == 1:
        spelling()
    elif test_type == 2:
        memorization()
    time.sleep(10)
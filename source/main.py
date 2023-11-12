import sys
from hideelems import hideelems
from seleniumbase import Driver as uc
from selenium.webdriver.common.keys import Keys as kys
from selenium.webdriver.common.by import By
from os import system


while True:
    print("Введите какой продукт ищем")
    inp1 = input()
    print('Введите от скольки отзывов показывать предложения')
    inp2 = input()
    while (not inp2.isdigit()):
        print('Введено не число. Введите число')
        inp2 = input()
    inp2 = int(inp2)
    pagenow = 1
    driver = uc(uc=True, browser='Chrome')
    driver.get("http://www.ozon.ru")
    while inp1 != 3:
        try:
            elem = driver.find_element(By.NAME, "text")
            elem.send_keys(inp1)
            elem.send_keys(kys.ENTER)
            hideelems(driver, inp2)
            while True:
                print("1.Предидущия страница.\n2.Следующая страница.\n3.Выход.\nВвод: ", end='')
                inp1 = input()
                while (inp1 != '1' and inp1 != '2' and inp1 != '3'):
                    print('Неправильный ввод. Попробуйте снова.\nВвод: ', end='')
                    inp1 = input()
                if inp1 == '1':
                    system('cls')
                    if pagenow == 1:
                        print('Вы и так на первой страничке')
                    else:
                        pagenow -= 1
                        elements = driver.find_elements(By.CLASS_NAME, 'e5q')
                        for i in elements:
                            if i.text == str(pagenow):
                                i.click()
                                hideelems(driver, inp2)
                                break
                elif inp1 == '2':
                    pagenow += 1
                    fl = True
                    elements = driver.find_elements(By.CLASS_NAME, 'e5q')
                    for i in elements:
                        if i.text == str(pagenow):
                            i.click()
                            hideelems(driver, inp2)
                            fl = False
                            break
                    system('cls')
                    if fl:
                        print('Вы и так на последней страничке')
                elif inp1 == '3':
                    driver.close()
                    sys.exit()
        except Exception as e:
            print("Error:", e)
            driver.close()
            sys.exit()

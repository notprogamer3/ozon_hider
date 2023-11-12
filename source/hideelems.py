import time
import sys
import seleniumbase
from selenium.webdriver.common.by import By

def hideelems(driver: seleniumbase.Driver, viewscompare):
    try:
        time.sleep(3)
        elements = driver.find_elements(By.CLASS_NAME, "i9u")
        todel='i9u'
        if len(elements) == 0:
            todel = 'i8u'
            elements = driver.find_elements(By.CLASS_NAME, "i8u")
        for i in range(len(elements)):
            elemsspis = elements[i].text.split('\n')
            views = 0
            for j in elemsspis:
                if 'отзыв' in j and 'балл' not in j:
                    views = int(''.join(j.split('  ')[1].split(' ')[0].split(' ')))
                    break
                else:
                    pass
            if views < viewscompare:
                driver.execute_script(f'return document.getElementsByClassName("{todel}")[{i}].style.display = "none"')
    except Exception as e:
        print("Error:", e)
        driver.close()
        sys.exit()

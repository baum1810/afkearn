from os import system
import time
import undetected_chromedriver as uc
import requests
from selenium.webdriver.common.by import By

#add your cookie here
cookie = "YOURCOOKIE"







# dont touch the shit under this line if u dont know what you are doing

# cookie check
target = "AskPython"
if "s%" not in cookie:
    print("YOU NEED TO IMPORT YOUR FLOW.TK COOKIE FOR THIS TO WORK! GOTO https://github.com/baum1810/flowi#setup")
    time.sleep(100)
else: options = uc.ChromeOptions()
driver = uc.Chrome()
driver.get('https://flow.tk/')
driver.add_cookie({'name' : 'COOKIE', 'value' : cookie})
driver.get('https://flow.tk')
links = 0

def main():
    global  links
    system("cls")
    print(f"Links: {links}")
    time.sleep(2)
    driver.execute_script('document.getElementById("generate").click()')
    time.sleep(2)

    driver.execute_script("document.querySelector('.btn.btn-primary.btn-block').click();")
    time.sleep(2)

    if "https://bstlar.com" in driver.current_url:
        for i in range(3):
            try:
                tabs = driver.window_handles
                driver.switch_to.window(tabs[0])
                driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/button').click()
                link1 = driver.page_source
                link1 = link1.split('https://entlyhaveb.autos/redirect?tid=')
                link1 = link1[1].split('" target="_BLANK')
                link1 = f"https://entlyhaveb.autos/redirect?tid={link1[0]}"
                driver.execute_script('''document.querySelector('a[href="'''+link1+'''"]').click();''')
                tabs = driver.window_handles
                driver.switch_to.window(tabs[1])
                driver.close()


            except:pass
        for i in range(3):
            try:
                tabs = driver.window_handles
                driver.switch_to.window(tabs[0])
                driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/button').click()
                link1 = driver.page_source
                link1 = link1.split('https://entlyhaveb.autos/redirect?tid=')
                link1 = link1[1].split('" target="_BLANK')
                link1 = f"https://entlyhaveb.autos/redirect?tid={link1[0]}"
                driver.execute_script('''document.querySelector('a[href="'''+link1+'''"]').click();''')
                tabs = driver.window_handles
                driver.switch_to.window(tabs[1])
                driver.close()
            except:pass
        for i in range(3):
            try:
                tabs = driver.window_handles
                driver.switch_to.window(tabs[0])
                driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/button').click()
                link1 = driver.page_source
                link1 = link1.split('https://searchwithme.net/redirect?tid=')
                link1 = link1[1].split('" target="_BLANK')
                link1 = f"https://searchwithme.net/redirect?tid={link1[0]}"
                driver.execute_script('''document.querySelector('a[href="'''+link1+'''"]').click();''')
                tabs = driver.window_handles
                driver.switch_to.window(tabs[1])
                driver.close()
            except:pass

        tabs = driver.window_handles
        driver.switch_to.window(tabs[0])
        while not "Unlock progress: 3 /" in driver.page_source:
            time.sleep(0.1)
        try:
            driver.find_element(By.XPATH, '/html/body/div[6]').click()
        except:
            driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div/div[4]/button').click()
        try:
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])
            driver.close()
            driver.switch_to.window(tabs[0])
        except:pass
    links += 1

while True:
    main()



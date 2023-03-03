from os import system
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

#add your cookie here
cookie = "YOURCOOKIE"
#domain of flow here they sometimes change the domain
domain = "https://flownew.vercel.app/"






# dont touch the shit under this line if u dont know what you are doing
options = uc.ChromeOptions()
options.add_argument("--disable-popup-blocking")
driver = uc.Chrome(options=options)
driver.get(domain)
driver.add_cookie({'name' : 'COOKIE', 'value' : cookie})
driver.get(domain)
links = 0

def main():
        try:
            
            global  links
            global domain
            tabs = driver.window_handles
            driver.switch_to.window(tabs[0])
            driver.get(domain)
    
            system("cls")
            print(f"Links: {links}")
            time.sleep(2)
            driver.execute_script('document.getElementById("generate").click()')
            time.sleep(2)
    
    
            while "Too many requests, please try again later." in driver.page_source:
                    time.sleep(10)
                    driver.get(domain)
            time.sleep(5)
            try:
                driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
                
            except:
                try:
                    driver.execute_script("document.querySelector('#qc-cmp2-ui > div:nth-child(2) > div > button:nth-child(2)').click();")
                except:pass
            try:
                driver.execute_script("""document.evaluate('/html/body/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();""")
            except:
                driver.execute_script("document.getElementById('destination-button').click();")
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])
            time.sleep(8)
            driver.execute_script("location.replace('https://flownew.vercel.app/reward?key=' + document.getElementById('tokenfield').value)")
            driver.switch_to.window(tabs[0])
            time.sleep(1)
            driver.close()
            links +=1
        except:
           
            main()
while True:
    main()

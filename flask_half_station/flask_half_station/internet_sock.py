
from selenium import webdriver
# 可以显示这个title控件
def internet_get(num):
    # 使用时需修改
    url='http://127.0.0.1:8080/web/L10/userinfoDelete.php?id='+str(num)
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # driver.find_element_by_id("text").send_keys(str(num))
    # driver.submit()
    htmltextget = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    return htmltextget

def internet_post(num):
    # 使用时需修改
    url='http://127.0.0.1:8080/web/L10/userinfoDelete.php'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    # driver.find_element_by_id("text").send_keys(str(num))
    # driver.submit()
    htmltextget = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()
    return htmltextget
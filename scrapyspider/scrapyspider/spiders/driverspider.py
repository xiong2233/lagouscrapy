from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def lgnum(url):
    path = './chromedriver.exe'
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get(url)
    num = driver.find_elements_by_xpath('//div[@class="pager_container"]//span[last()-1]')[0].text
    driver.close()
    driver.quit()
    print(num)



# -*- coding: utf-8 -*-
import scrapy
import time
import re
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapyspider.items import ScrapyspiderItem


class ScaspiderSpider(RedisSpider):
    name = 'ScaSpider'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    redis_key = 'lagou:start_urls'
    # path = 'E:\chromedriver.exe'
    List = []
    # def parse(self, response):
        # job = input("请输入职位：")
        # url = self.baseurl[0] + job
        # print(url)
        # yield scrapy.Request(self.start_urls,meta={'url': self.start_urls},callback=self.one_parse)
    url = 'https://www.lagou.com/jobs/list_python'
    print(url)
    def parse (self,response):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        time.sleep(1)
        num = driver.find_elements_by_xpath('//div[@class="pager_container"]//span[last()-1]')[0].text
        nums = driver.find_element_by_class_name('pager_is_current')
        html = driver.page_source
        zhi = re.findall('"pager_next "',html)
        if zhi != []:
            for x in range(int(num)-1):
                driver.execute_script(
                    'window.scrollTo(0,document.body.scrollHeight)'
                )
                time.sleep(3)
                href = driver.find_elements_by_class_name('position_link')
                print("是否执行")
                for oneurl in href:
                    try:
                        twourl = oneurl.get_attribute('href')
                        # print(twourl)
                        yield scrapy.Request(twourl, callback=self.two_parse)
                    except Exception as e :
                        print("实在是无法获取数据")
                print("执行了")
                driver.find_element_by_class_name('pager_next ').click()
                time.sleep(4)
                print("点击过后")
        else:
            print("只有一页")
            href = driver.find_elements_by_class_name('position_link')
            print("是否执行")
            for oneurl in href:
                try:
                    twourl = oneurl.get_attribute('href')
                    # print(twourl)
                    yield scrapy.Request(twourl,meta={'url':twourl},callback=self.two_parse)
                except Exception as e:
                    print("实在是无法获取数据")
    # def num_parse(self,driver):


    def two_parse(self,response):
        item = ScrapyspiderItem()
        # url = response.url
        # print(response.url)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--no-sandbox")
        urls = response.meta
        if 'redirect_urls' in urls:
            url = urls['redirect_urls'][0]
            print(url)
            # https: // passport.lagou.com / login / login.html?msg = validation & uStatus = 2 & clientIp = 183.226.198.12
            driver_two = webdriver.Chrome(options=chrome_options)
            driver_two.get(url)
            # print(driver_two.current_url)
            if "https://passport.lagou.com/login/login.html" in driver_two.current_url:
                print("要登录")
                driver_two.find_element_by_xpath('//input[@type="text"]').send_keys('电话号码')
                driver_two.find_element_by_xpath('//input[@type="password"]').send_keys('密码')
                driver_two.find_element_by_xpath('//input[@type="submit"]').click()
                time.sleep(1)
                driver_two.get(url)
                time.sleep(1)
                cname = driver_two.find_elements_by_xpath('//div[@class="company"]')
                if cname == []:
                    item['cname'] = "无公司信息"
                else:
                    item['cname'] = driver_two.find_elements_by_xpath('//div[@class="company"]')[0].text
                title = driver_two.find_elements_by_xpath('//div[@class="job-name"]//span[@class="name"]')
                if title == []:
                    item['title'] = "无标题"
                else:
                    item['title'] = driver_two.find_elements_by_xpath('//div[@class="job-name"]//span[@class="name"]')[0].text
                require = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p//span')
                item['requires'] = ""
                for re in require:
                    item['requires'] += re.text.replace(' ', '')
                input_time = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p[@class="publish_time"]')
                if input_time == []:
                    item['input_time'] = '暂无数据'
                else:
                    item['input_time'] = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p[@class="publish_time"]')[0].text.replace(' ', '')
                lure = driver_two.find_elements_by_xpath('//div[@class="content_l fl"]//dl[@id="job_detail"]//dd[@class="job-advantage"]//p')
                if lure == []:
                    item['lure'] = "暂时无数据"
                else:
                    item['lure'] = driver_two.find_elements_by_xpath('//div[@class="content_l fl"]//dl[@id="job_detail"]//dd[@class="job-advantage"]//p')[0].text.replace(' ', ',')
                item['repr'] = driver_two.find_element_by_class_name('job_bt')
                if item['repr'] == []:
                    item['repr'] = '无数据'
                else:
                    item['repr'] = driver_two.find_element_by_class_name('job_bt').text.replace('\n', ' ')
                address = driver_two.find_elements_by_xpath('//div[@class="work_addr"]')
                item['addr'] = ""
                for ad in address:
                    if ad.text.strip() != "\n":
                        adr = ad.text.replace('\n', '').strip().replace(" ", '')
                        if adr != '查看地图':
                            item['addr'] += adr
                print(item['cname'], item['title'], item['requires'], item['input_time'], item['lure'], item['repr'],item['addr'])
                yield item
            else:
                cname = driver_two.find_elements_by_xpath('//div[@class="company"]')
                if cname == []:
                    item['cname'] = "无公司信息"
                else:
                    item['cname'] = driver_two.find_elements_by_xpath('//div[@class="company"]')[0].text
                title = driver_two.find_elements_by_xpath('//div[@class="job-name"]//span[@class="name"]')
                if title == []:
                    item['title'] = "无标题"
                else:
                    item['title'] = driver_two.find_elements_by_xpath('//div[@class="job-name"]//span[@class="name"]')[0].text
                require = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p//span')
                item['requires'] = ""
                for re in require:
                    item['requires'] += re.text.replace(' ', '')
                input_time = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p[@class="publish_time"]')
                if input_time == []:
                    item['input_time'] = '暂无数据'
                else:
                    item['input_time'] = driver_two.find_elements_by_xpath('//dd[@class="job_request"]//p[@class="publish_time"]')[0].text.replace(' ', '')
                lure = driver_two.find_elements_by_xpath('//div[@class="content_l fl"]//dl[@id="job_detail"]//dd[@class="job-advantage"]//p')
                if lure == []:
                    item['lure'] = "暂时无数据"
                else:
                    item['lure'] = driver_two.find_elements_by_xpath('//div[@class="content_l fl"]//dl[@id="job_detail"]//dd[@class="job-advantage"]//p')[0].text.replace(' ', ',')
                item['repr'] = driver_two.find_element_by_class_name('job_bt')
                if item['repr'] == []:
                    item['repr'] = '无数据'
                else:
                    item['repr'] = driver_two.find_element_by_class_name('job_bt').text.replace('\n',' ')
                address = driver_two.find_elements_by_xpath('//div[@class="work_addr"]')
                item['addr'] = ""
                for ad in address:
                    if ad.text.strip() != "\n":
                        adr = ad.text.replace('\n', '').strip().replace(" ", '')
                        if adr != '查看地图':
                            item['addr'] += adr
                print(item['cname'],item['title'],item['requires'],item['input_time'],item['lure'],item['repr'],item['addr'])
            yield item
        else:
            pass

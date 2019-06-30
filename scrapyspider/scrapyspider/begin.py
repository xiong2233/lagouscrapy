from scrapy import cmdline
import time
cmdline.execute('scrapy crawl ScaSpider -o scaspider.json'.split())
# time.sleep(2)
#
# import redis
# redisArgs={
#     'host':'148.70.182.173',
#     'port':6379,
#     "db":'lagou'
# }
#
# re = redis.Redis(**redisArgs)
# job = input("请输入你要查询的职位：")
# url = "https://www.lagou.com/jobs/list_" + job
# re.set('start_urls',url)

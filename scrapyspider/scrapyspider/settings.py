# -*- coding: utf-8 -*-

# Scrapy settings for scrapyspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyspider'

SPIDER_MODULES = ['scrapyspider.spiders']
NEWSPIDER_MODULE = 'scrapyspider.spiders'

FEED_EXPORT_ENCODING = 'utf-8'
# * 使用scrapy_redis调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# * 使用scrapy_redis去重机制
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Host': 'www.lagou.com',
  'Referer': 'https://www.lagou.com/jobs/list_Python',
  'Upgrade-Insecure-Requests': 1,
  'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    # 'scrapyspider.middlewares.ScrapyspiderSpiderMiddleware': 543,
#   'scrapyspider.middlewares.scpiderM':543
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
   # 'scrapyspider.middlewares.ScrapyspiderDownloaderMiddleware': 543,
   # 'scrapyspider.middlewares.dowmM':543
    # 'scrapyspider.middlewares.MyScrapyspiderDownloaderMiddleware':600,
    # 'scrapy.downloadermiddleware.useragent.UserAgentMiddleware':None,
    # 'scrapyspider.middlewares.MyUserAgentMiddleware':300
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 300,
   # ''
}
REDIS_HOST = '公网ip'
REDIS_POST = 6379
REDIS_PARAMS = {'password':'test123'}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'lagoudb'
MONGO_SET = 'lagouset'


# user_agent_list = [
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
#         "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#         "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
#         "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
#         "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
#         "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
#         "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
#         "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
#         "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#         "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
#         "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
#         "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]
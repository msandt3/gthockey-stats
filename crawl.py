from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log,signals
from scrapy.xlib.pydispatch import dispatcher
from stats.spiders.acha import AchaSpider


def stop():
	reactor.stop()

dispatcher.connect(stop, signal=signals.spider_closed)
spider = AchaSpider()
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run() # the script will block here
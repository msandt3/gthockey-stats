from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log,signals
from scrapy.xlib.pydispatch import dispatcher
from stats.spiders.acha import AchaSpider




def stop():
	reactor.stop()

# listen for spider closed signal & stop reactor
dispatcher.connect(stop, signal=signals.spider_closed)



spider = AchaSpider()
crawler = Crawler(Settings({'LOG_ENABLED':'True', 'ITEM_PIPELINES':'stats.pipelines.StatsPipeline'}))
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run() # the script will block here
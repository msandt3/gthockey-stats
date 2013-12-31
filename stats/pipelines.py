# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log,signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy.xlib.pydispatch import dispatcher

class StatsPipeline(object):

	def __init__(self):
		self.files = {}
		dispatcher.connect(self.spider_opened, signals.spider_opened)
		dispatcher.connect(self.spider_closed, signals.spider_closed)
	def spider_opened(self,spider):
		file = open('stats.json','wb')
		self.files[spider] = file
		self.exporter = JsonItemExporter(file)
		self.exporter.start_exporting()
	def spider_closed(self,spider):
		self.exporter.finish_exporting()
		file = self.files.pop(spider)
		file.close()
	def process_item(self, item, spider):
		# determine if the name has a * in it & remove it
		if item['name']:
			if "* " in item['name']:
				item['name'].replace("* ","",1)
		self.exporter.export_item(item)
		return item

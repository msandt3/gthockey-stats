# Scrapy settings for stats project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#



BOT_NAME = 'stats'

SPIDER_MODULES = ['stats.spiders']
NEWSPIDER_MODULE = 'stats.spiders'



#Enable log and set up custom item pipeline
LOG_ENABLED = True 
ITEM_PIPELINES = ['stats.pipelines.StatsPipeline']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stats (+http://www.yourdomain.com)'

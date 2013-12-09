# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class StatsItem(Item):
    name = Field()
    number = Field()
    gamesPlayed = Field()
    goals = Field()
    assists = Field()
    points = Field()
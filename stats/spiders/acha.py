from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from stats.items import StatsItem

class AchaSpider(BaseSpider):
    name = 'acha'
    allowed_domains = ['acha.org']
    start_urls = ['http://achahockey.org/player_roster.php?team_id=13007&league_id=1063']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        rows = hxs.select("//*[@id='pg_content']/table[2]/tr")
        items = []

        i = 0
        for row in rows:
            if i != 0:
                item = StatsItem()
                item['name'] = row.select("td[2]/a/text()").extract()
                item['number'] = row.select("td[1]/text()").extract()
                item['gamesPlayed'] = row.select("td[3]/text()").extract()
                item['goals'] = row.select("td[4]/text()").extract()
                item['assists'] = row.select("td[5]/text()").extract()
                item['points'] = row.select("td[6]/text()").extract()
                items.append(item)
            i += 1
        return items          
import scrapy
from switchgames.items import SwitchgamesItem
import re
from datetime import datetime

class GamesSpider(scrapy.Spider):
    name = "SwitchGames"
    start_urls = ['https://www.eurogamer.net/archive/switch']
    npages = 100
    for n in range(100, npages + 200, 100):
        start_urls.append('https://www.eurogamer.net/archive/switch?start=' + str(n))


    def parse(self, response):
        for href in response.xpath("//h2[contains(@class, 'title')]/a//@href"):
            url  = "https://www.eurogamer.net" + href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = SwitchgamesItem()

        # Getting SwitchGame News Title, Date and Comments
        item['newsTitle'] = response.xpath("//h1[@class='title']/text()").extract()
        item['newsDate']= response.xpath("//article/header/div/div[3][@class='date']/span/text()").extract()
        comment_list = response.xpath("//div[@id='comments']/p[@class='section-title']/text()").extract()
        for x in comment_list:
            x = re.findall('\d+', x)
            item['newsComments'] = x

        # Url (The link to the news page)
        item['newsUrl'] = response.xpath("//meta[@property='og:url']/@content").extract()

        yield item


"""
# start page
https://www.eurogamer.net/archive/switch
# from second page on
https://www.eurogamer.net/archive/switch?start=100
https://www.eurogamer.net/archive/switch?start=200
https://www.eurogamer.net/archive/switch?start=300

# News page url sample
https://www.eurogamer.net/articles/2020-07-28-paper-mario-invades-tetris-99-for-next-special-cup
"""

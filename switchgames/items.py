# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SwitchgamesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    newsTitle = scrapy.Field()
    newsDate = scrapy.Field()
    newsComments = scrapy.Field()
    newsUrl = scrapy.Field()

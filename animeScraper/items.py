# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimescraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field() # anime title
    link = scrapy.Field() # Link to MAL entry
    sscore = scrapy.Field() # Score from site
    date = scrapy.Field() # Date released
    genres = scrapy.Field() # Genres of anime
    pass

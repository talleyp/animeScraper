from scrapy.spiders import XMLFeedSpider
from animeScraper.items import AnimescraperItem

class MySpider(XMLFeedSpider):
    name = 'myanimelist'
    allowed_domains = ['myanimelist.net']
    start_urls = ['https://myanimelist.net/malappinfo.php?u=shaliber&status=all&type=anime']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        item = Items()

        item['title'] = node.select('series_title').extract()
        print(item['title'])

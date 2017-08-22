import scrapy

class TorrentSpider(scrapy.Spider):
    name = "torrents"
    url = 'https://nyaa.si/?page=rss&c=1_2&f=2'

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)


    def parse(self, response):
        descriptions = response.xpath('//item//description').extract()
        filename = "torrentAnimeTitle"
        for description in descriptions:
            splitDescription = description.split("|")
            title = splitDescription[1]
            magnet = splitDescription[4]
            print(dict(title=title, magnet=magnet))

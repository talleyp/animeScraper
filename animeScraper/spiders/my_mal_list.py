import scrapy

class MyListSpider(scrapy.Spider):
    name = "anime"
    url = 'https://myanimelist.net/animelist/Shaliber'

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)


    def parse(self, response):
        animes = response.xpath('//tbody[@class=list-item]')
        filename = "AnimeTitles"
        for anime in animes:
            title = anime.xpath('//table//tr//td[@class="data title clearfix"]\
                                //a/@href').extract_first()
            print(dict(title=title))

import scrapy


class MyListSpider(scrapy.Spider):
    name = "mylist"

    def start_requests(self):
        urls = [
            'https://myanimelist.net/animelist/Shaliber',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'myAnimeList.html' 
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

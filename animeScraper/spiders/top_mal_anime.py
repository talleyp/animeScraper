import scrapy

class TopAnimeSpider(scrapy.Spider):
    name = "topanime" # Name of the spider, to be used when crawling
    allowed_domains = ["myanimelist.net"] # Where the spider is allowed to go
    url = "https://myanimelist.net/topanime.php"

    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)

    def parse(self, response):
        for href in response.css('.ranking-list a.hoverinfo_trigger::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_anime)

        next_page = response.css('.pagination a.next::attr(href)').extract_first()
        if next_page is not None:
            next_page = self.url + next_page
            yield scrapy.Request(next_page, self.parse)

        def parse_anime(self, response):
            slug = reponse.url.split('/')
            slug = slug[len(slug) - 1].replace('_','-').lower()

            sscore = response.css('.anime-detail-header-stats .score::text').extract_first()
            sscore = float(rating.rstrip())

            title = response.css('h1 span::text').extract_first()

            date =

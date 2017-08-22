import scrapy
import re

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
        link = response.url

        sscore = response.css('.anime-detail-header-stats .score::text').extract_first()
        sscore = float(sscore.rstrip())

        title = response.css('h1 span::text').extract_first()

        date = ''
        date_elements = response.xpath('//div[@class="spaceit"]/text()').extract()
        for elem in date_elements:
            clean_elem = elem.strip()
            if re.match(r'\d{4]',clean_elem[-4:]):
                date = clean_elem
                print(date)

        genres = response.xpath('//a[contains(@href, "genre")]/text()').extract()

        yield {
            'link': link,
            'title': title,
            'date': date,
            'sscorescr': sscore,
            'genres': genres
            }

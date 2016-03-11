import scrapy
from tutorial.items import ProfessorItem


class UIUCSpider(scrapy.Spider):
    name = "uiuc"
    start_urls = [
        "https://www.cs.utexas.edu/faculty",
    ]

    def parse(self, response):
        for sel in response.css('.views-row'):
            profName = sel.css('.prof-name::text').extract().strip()
            if profName:
                item = ProfessorItem()
                item['name'] = profName
                yield item

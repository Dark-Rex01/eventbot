import scrapy
from ..items import WebautoItem

class HackSpider(scrapy.Spider):
    name = 'hackevents'
    start_urls = {
        "https://www.hackerearth.com/challenges/"
    }
    def parse(self, response):
        items = WebautoItem()
        all_div = response.css('div.upcoming.challenge-list')
        upcoming = all_div.css('.challenge-card-modern')

        for hackevents in upcoming:

            title = hackevents.css('span.challenge-list-title.challenge-card-wrapper::text').extract()
            dates = hackevents.css('.date.less-margin.dark::text').extract()

            items['title'] = title
            items['dates'] = dates
            items['webname'] = 'hackerearth'
            items['website'] = 'https://www.hackerearth.com/challenges/'

            yield items





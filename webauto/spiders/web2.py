import scrapy
from ..items import WebautoItem

class HackSpider(scrapy.Spider):
    name = 'hackeventss'
    start_urls = {
        "https://mlh.io/seasons/2021/events"
    }
    def parse(self, response):

        items = WebautoItem()
        sel = response.css('div.row')[1]
        all_div = sel.css('div.event-wrapper')

        for hackevents in all_div:

            title = hackevents.css('.event-name::text').extract()
            dates = hackevents.css('.event-date::text').extract()

            items['title'] = title
            items['dates'] = dates
            items['webname'] = 'Major hacking League'
            items['website'] = 'https://mlh.io/seasons/2021/events'

            yield items


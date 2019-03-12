import scrapy
from ..items import AppleItem

class AppleSpider(scrapy.Spider):
    name = 'apple'
    # start_urls = ['https://tw.appledaily.com/new/realtime']

    def start_requests(self):
        url = 'https://tw.appledaily.com/new/realtime/%s'
        for i in range(1, 3):
            print('[Page]', url % str(i))
            yield scrapy.Request(url % str(i), callback=self.parse)

    def parse(self, response):
        items = []
        list = response.css('ul.slvl li')
        for li in list:
            item = AppleItem()
            item['url'] = li.css('a::attr(href)').extract_first()
            item['title'] =  li.css('font::text').extract_first()
            item['view'] = str(li.css('span::text').extract_first())[1:-1]
            items.append(item)

            print('[T1]', item['title'])
            yield scrapy.Request(item['url'], callback=self.parse_detail)
        return items

    def parse_detail(self, response):
        print('[T2]', response.css('h1::text').extract_first())
        

# -*- coding: utf-8 -*-
import scrapy
import time
from ptt.items import PttItem

class ArticleSpider(scrapy.Spider):
    name = 'article'
    # allowed_domains = ['ptt.cc']
    # start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']

    def start_requests(self):
        yield scrapy.Request('https://www.ptt.cc/bbs/Gossiping/index.html', 
                             method='get', 
                             cookies={'over18':'1'}, 
                             callback=self.parse_entry)

    def parse_entry(self, response):
        pre_page = response.css('div.btn-group-paging a::attr(href)')[1].extract()
        num_of_pre_page = int(pre_page.split('/')[-1].replace('index', '').replace('.html', '')) + 1
        
        for i in range(0, 3):
            print('[ Page ]', (num_of_pre_page - i))
            url = 'https://www.ptt.cc/bbs/Gossiping/index' + str(num_of_pre_page - i) + '.html'
            yield scrapy.Request(url,
                                method='get', 
                                cookies={'over18':'1'}, 
                                callback=self.parse_article)

    def parse_article(self, response):
        print('---')
        item = PttItem()
        targets = response.css("div.r-ent")
        for target in targets:
            try:
                item['title'] = target.css('div.title a::text')[0].extract()
                item['author'] = target.css('div.author::text')[0].extract()
                item['date'] = target.css('div.date::text')[0].extract()
                #item['push'] = target.css('div.nrec span::text')[0].extract()
                item['url'] = target.css('div.title a::attr(href)')[0].extract()
                print('[[ Title ]]', item['title'])
                yield item
            except IndexError:
                pass
            continue

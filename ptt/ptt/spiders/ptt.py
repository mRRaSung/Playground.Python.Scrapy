import scrapy
import logging
from scrapy.http import FormRequest

class PttSpider(scrapy.Spider):
    name = 'ptt'
    allow_domain = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Gossiping/index.html']

    _retries = 0    # 嘗試次數
    MAX_RETRY = 1   # 最多嘗試次數

    def parse(self, response):

        # urljoin 範例
        # print('[Response]', response)
        # print('[Join]', response.urljoin('helloworld.html'))

        # 另存檔案
        # filename = response.url.split('/')[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # 檢查是否為確認年紀的頁面
        if(len(response.css('div.over18-notice')) > 0):
            print('Check !')

            if(self._retries < self.MAX_RETRY):
                self._retries += 1
                logging.error('retry {} times...'.format(self._retries))
                yield FormRequest.from_response(response, 
                                                formdata = { 'yes' : 'yes' },
                                                callback=self.parse)
            else:
                logging.error('you can not pass !')
        else:
            print('Already !')

            for href in response.css('.r-ent > div.title > a::attr(href)'):
                url = response.urljoin(href.extract())
                print('[href]{} [url]{}'.format(href.extract(), url))
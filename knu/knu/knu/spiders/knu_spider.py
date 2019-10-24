# -*- coding: utf-8 -*-
import scrapy
import sys
from knu.items import KnuItem
from scrapy.selector import HtmlXPathSelector
from scrapy import Request

class KnuSpider(scrapy.Spider):
		name = 'knu'
		allowed_domains = ['kongju.ac.kr']
		start_urls = ['http://www.kongju.ac.kr/lounge/board.jsp?board=student_news']

		def start_requests(self):
				headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
				for url in self.start_urls:
					yield Request(url, headers=headers)
		
		def parse(self, response):
				item = KnuItem()
				for sel in response.xpath('//table[@class="content_main_table02"]//tr'):
					item['title'] = sel.xpath('/td[2]/a/b/font/text()').extract()
					item['link'] = sel.xpath('/td[2]/a/@href').extract()
					item['date'] = sel.xpath('/td[5]/text()').extract()
					yield item

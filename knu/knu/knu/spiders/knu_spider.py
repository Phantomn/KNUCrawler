# -*- coding: utf-8 -*-
import scrapy
import sys
from knu.items import KnuItem

class KnuSpider(scrapy.Spider):
	name = 'knu'
	allowed_domains = ['kongju.ac.kr']
	start_urls = ['http://www.kongju.ac.kr/lounge/board.jsp?board=student_news']

	def parse(self, response):
		item = KnuItem()
		for sel in response.xpath('//div[@id="container"]//div[@id="colgroub"]//div[@id="content_new"]/form/table[@class="content_main_table02"]//tr[@class="table_tr"]'):
			item['title'] = sel.xpath('//td[2]/a/@title').extract()
			item['link'] = sel.xpath('//td[2]/a/@href').extract()
			item['date'] = sel.xpath('//td[5]/text()').extract()
			yield item

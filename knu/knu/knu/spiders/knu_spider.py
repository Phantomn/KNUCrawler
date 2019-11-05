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
		for i in range(1,16):
			for sel in response.xpath('//div[@id="container"]//div[@id="colgroub"]//div[@id="content_new"]/form/table[@class="content_main_table02"]//tr[@class="table_tr"]['+str(i)+']'):
				item['title'] = sel.xpath('//td[2]/a/@title')[i-1].extract()
				item['link'] = "http://www.kongju.ac.kr/lounge/" + sel.xpath('//td[2]/a/@href')[i-1].extract()
				item['date'] = sel.xpath('//td[5]/text()')[i-1].extract()
				yield item

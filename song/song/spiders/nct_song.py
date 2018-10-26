# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import HtmlResponse

#official = '<span class="icon-tag-official" title="Bản Chính Thức">Official</span>'
#official = 'logo-official'

class NctSongSpider(CrawlSpider):
	name = 'nct_song'
	allowed_domains = ['nhaccuatui.com']

	start_urls = pd.read_csv('/home/tuananh2998/Documents/python/crawldone/song_list.csv', header=0).values[:,0]

	#def parse(self, response): 
	#	for li in response.xpath('/html/body/div[9]/div/div/div[1]/div[1]/ul/li').extract():
	#		if official in li:
	#			link = HtmlResponse(url='', body=li, encoding='utf8').xpath('/div[2]/a[1]').extract()
	#			yield {'url': link, 'type': 'song'}

	def parse(self, response):
		for link in response.xpath('/html/body/div[9]/div/div/div[1]/div[1]/ul/li/a[1]/@href').extract():
	#		yield scrapy.Request(link, callback=self.parse_song)
	
	#def parse_song(self, response):
	#	url = response.url
	#	if 'logo-official' in response.xpath('/html/body/div[6]/div[2]/div/div[1]/div[6]/div/div/span[1]').extract():
			yield {'url': link, 'type': 'song'}

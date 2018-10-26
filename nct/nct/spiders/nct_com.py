# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import HtmlResponse


class NctComSpider(CrawlSpider):
	name = 'nct_com'
	allowed_domains = ['nhaccuatui.com']


	start_urls = pd.read_csv('/home/tuananh2998/Documents/python/crawldone/artists.csv', header=0).values[:,0]
	start_urls = [url.replace('.html', '.bai-hat.html') for url in start_urls]

	rules = [
		#Rule(LinkExtractor(allow=('.*\/nghe-si[-!0-9a-z]+\.html')),
			#follow=True, callback='parse_artist_profile'),
		Rule(LinkExtractor(allow=('.*\/nghe-si[-a-zA-Z0-9]+\.bai-hat\.[1-9]+.*')),
			follow=True, callback='parse_artist_playlist'),
		#Rule(LinkExtractor(allow=('.*\/bai-hat\/[-1-9a-zA-Z]+\.[0-9a-zA-Z]+\.html')),
		#	follow=True, callback='parse_song'),	
	]

	
	#def parse_artist_profile(self, response):
		#url=response.url
		#yield {'url': url, 'type': 'tieu-su'}
	
	def parse_artist_playlist(self, response):
		url=response.url
		yield {'url': url, 'type': 'song-list'}	

	#def parse(self, response):
		#url=response.url
		#yield {'url': url, 'type': 'song-list'}
	#	for li in response.css('body > div:nth-child(12) > div > div > div.box-left > div > ul > li').extract():
	#		if official in li: 
	#			link = HtmlResponse(url="tmp", body=li, encoding='utf8').css('div.item_content > h3 > a::attr(href)').extract_first()
	#			yield {'url': link, 'type': 'song'}

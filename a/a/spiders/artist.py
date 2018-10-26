# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ArtistSpider(CrawlSpider):
    name = 'artist'
    allowed_domains = ['nhaccuatui.com']
    start_urls = [
	'https://www.nhaccuatui.com/nghe-si/a.html',
	'https://www.nhaccuatui.com/nghe-si/b.html',
	'https://www.nhaccuatui.com/nghe-si/c.html',
	'https://www.nhaccuatui.com/nghe-si/d.html',
	'https://www.nhaccuatui.com/nghe-si/e.html',
	'https://www.nhaccuatui.com/nghe-si/f.html',
	'https://www.nhaccuatui.com/nghe-si/g.html',
	'https://www.nhaccuatui.com/nghe-si/h.html',
	'https://www.nhaccuatui.com/nghe-si/i.html',
	'https://www.nhaccuatui.com/nghe-si/j.html',
	'https://www.nhaccuatui.com/nghe-si/k.html',
	'https://www.nhaccuatui.com/nghe-si/l.html',
	'https://www.nhaccuatui.com/nghe-si/m.html',
	'https://www.nhaccuatui.com/nghe-si/n.html',
	'https://www.nhaccuatui.com/nghe-si/o.html',
	'https://www.nhaccuatui.com/nghe-si/p.html',
	'https://www.nhaccuatui.com/nghe-si/q.html',
	'https://www.nhaccuatui.com/nghe-si/r.html',
	'https://www.nhaccuatui.com/nghe-si/s.html',
	'https://www.nhaccuatui.com/nghe-si/t.html',
	'https://www.nhaccuatui.com/nghe-si/u.html',
	'https://www.nhaccuatui.com/nghe-si/v.html',
	'https://www.nhaccuatui.com/nghe-si/w.html',
	'https://www.nhaccuatui.com/nghe-si/x.html',
	'https://www.nhaccuatui.com/nghe-si/y.html',
	'https://www.nhaccuatui.com/nghe-si/z.html',
    ]

    rules = [
	Rule(LinkExtractor(allow=('.*\/nghe-si[-!0-9a-zA-Z]+\.html')), follow=True, callback='parse_artist_profile'),
    ]
    
    def parse_artist_profile(self, response):
        url=response.url
        yield {'url': url, 'type': 'tieu-su'}

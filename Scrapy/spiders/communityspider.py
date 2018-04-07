#-*- coding: utf-8 -*-

import scrapy

from community.items import CommunityItem
import datetime

class CommunitySpider(scrapy.Spider):
     name = "communityCrawler"


     def start_request(self):
          for i in range(1, 5, 1):
               yield scrapy.Request("https://www.clien.net/service/board/park?&od=T31&po=%d" % i, self.parse_clien)

     def pasrse_clien(self, response):
          for sel in response.xpath('//*[@id="div_content"]'):
               item = CommunityItem()

               item['souce'] = "클리앙"
               item['category'] = "free"
               item['title'] = sel.xpath('//*[@id="div_content"]/div[8]/div[2]/a[1]/span').extract()[0]
               item['url'] =  "https://www.clien.net" + sel.xpath('//*[@id="div_content"]/div[8]/div[2]/a[1]/@href').extract()[0][:2]
               item['date'] = sel.xpath('//*[@id="div_content"]/div[8]/div[5]/span/span')
               # dateTmp = datetime.strptime(sel.xpath('td/span/@title').extract()[0], "%Y-%n-%d %H:%M:%S ")
               # item['date'] = dateTmp.strftime("Y% - %m - %d %H:%M:%S")

               print ('=' *50)
               print (item['title'])

               yield item



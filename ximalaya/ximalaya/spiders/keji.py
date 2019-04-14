# -*- coding: utf-8 -*-
import json
import urllib.request
import scrapy

from ximalaya.items import XimalayaItem


class ItkejiSpider(scrapy.Spider):
    name = 'keji'
    allowed_domains = ['ximalaya.com']
    start_urls = ['https://www.ximalaya.com/keji/p1/']

    def parse(self, response):
        caritems = response.xpath("//div[@class='content']//li//a[@class='album-title line-1 lg bold _kC']/@href")
        cla = response.xpath('//ul[@class="bread-crumb-drop-list _Cz"]/li[@class="_Cz"]/a[@class="bread-crumb-link _Cz"]/text()').getall()

        item = XimalayaItem(cla=cla)

        yield item

        caritems = response.xpath("//div[@class='content']//li//a[@class='album-title line-1 lg bold _kC']/@href")
        for caritem in caritems:
                urls = caritem.re("\d+")[0]
                url = f"https://www.ximalaya.com/revision/play/album?albumId={urls}&pageNum=1&pageSize=30"
                yield scrapy.Request(url=url, callback=self.cardetails)
                for i in range(1, 35):
                    yield scrapy.Request(
                     url=f'https://www.ximalaya.com/keji/p{i}/', callback=self.parse)



    def cardetails(self, response):

        r = json.loads(response.text)
        rlists=r['data']['tracksAudioPlay']
        for i in range(len(rlists)):
            print(rlists[i]['src'])
            urllib.request.urlretrieve(rlists[i]['src'],'./m4a4/'+rlists[i]['trackName']+'.mp4')

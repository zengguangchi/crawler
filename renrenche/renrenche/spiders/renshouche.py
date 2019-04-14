# -*- coding: utf-8 -*-
import re

import scrapy
import time

from renrenche.items import RenrencheItem


class RenshoucheSpider(scrapy.Spider):
    name = 'renshouche'
    allowed_domains = ['renrenche.com']
    start_urls = ['https://www.renrenche.com/sz/ershouche/']

    def parse(self, response):


        # yield scrapy.Request(url=new_url,callback=self.parse_detail)
        brans = response.xpath('//div[@id="brand_more"]/div[@id="brand_more_content"]/div/p//a')

        for bran in brans:
            brandname = bran.xpath('./text()').get()
            print(type(brandname))
            item = RenrencheItem(name=brandname)
            yield item


        url ='https://www.renrenche.com/sz/ershouche/'

        yield scrapy.Request(url=url, callback=self.parse_url)



    def parse_url(self,response):
        brans = response.xpath('//div[@id="brand_more"]/div[@id="brand_more_content"]/div/p//a')
        for bran in brans:
            ur = bran.xpath('./@href').get()
            url = 'https://www.renrenche.com'+ur
            request = scrapy.Request(url=url, callback=self.parse_brand)
            yield request
    def parse_brand(self, response):
        carts = response.xpath('//ul[@class="row-fluid list-row js-car-list"]/li/a/@href').getall()
        for cart in carts:
            new_url = 'https://www.renrenche.com' + cart
            # time.sleep(1)
            yield scrapy.Request(url=new_url, callback=self.parse_detail)


    def parse_detail(self, response):
        titl = response.xpath('//div[@class="title"]/h1/text()').getall()
        titl2 = titl[1]
        title=titl2.strip()
        city = response.xpath('//div[@class="licensed-city"]/p[1]/strong[@id="car-licensed"]/text()').get()

        small = response.xpath('//li[@class="span7"]/div/p[1]/strong[@class="car-summary"]/text()').get()
        summary = response.xpath('//li[@class="kilometre"][2]/div/p[1]/strong[@class="car-summary"]/text()').get()
        travel = response.xpath('//div/p/strong/text()').get()
        price = response.xpath('//div/p[@class="price detail-title-right-tagP"]/text()').get()
        # print(cartid,title,city,small,summary,travel,price)
        item=RenrencheItem(city=city,small=small,summary=summary,travel=travel,price=price,title=title)

        yield item

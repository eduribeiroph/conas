# -*- coding: utf-8 -*-
import scrapy


class C01Spider(scrapy.Spider):
    name = "c01"
    start_urls = ['http://www.comprasnasantaifigenia.com.br/']

    def parse(self, response):
        items = response.xpath(
            '/html/body/div[1]/div[2]/div[1]/div[1]/ul'
        )
        for item in items:
            url = item.xpath('./li/a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
            
    def parse_detail(self, response):
        title = response.xpath('//*[@id="interna"]/div[1]/h5/strong/text()').extract_first()
        yield {
            'title': title,
            }
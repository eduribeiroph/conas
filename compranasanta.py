# -*- coding: utf-8 -*-
import scrapy


class CompranasantaSpider(scrapy.Spider):
    name = "compranasanta"
    allowed_domains = ["www.comprasnasantaifigenia.com.br/interna.asp?depto=acessorios"]
    start_urls = ['http://www.comprasnasantaifigenia.com.br/interna.asp?depto=acessorios/']

    def parse(self, response):
        divs = response.xpath('/html/body/div[1]/div[2]/div[2]')
        for div in divs:
           
           categoria = div.xpath(".//h3/text()").extract()
            title = div.xpath(".//div[1]/div/h5").extract()
            endereco = div.xpath(".//div[1]/div/div/div[1]/p/text()").extract()
            bairro = div.xpath(".//div[1]/div/div/div[2]/p/text()").extract()
            tel = div.xpath(".//div[1]/div/div/div[3]/div/p/text()).extract()
            href = div.xpath(".//div[1]/div/div/div[5]/div/p/a/text()").extract()
            yield {
               'categoria' : categoria,
                'title': title,
                'endereco': endereco,
                'bairro': bairro,
                'tel': tel,
                'url': href,
            }
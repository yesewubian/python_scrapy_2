# -*- coding: utf-8 -*-
import scrapy
from boya.items import BoyaItem

class BoyaSpider(scrapy.Spider):
    name = "boya"
    allowed_domains = ["bytravel.cn"]
    domain = 'http://shop.bytravel.cn'
    #allowed_domains = ["localhost"]
    start_urls = (
        'http://shop.bytravel.cn/',
        #'http://shop.bytravel.cn/produce/index141_list.html',
        #"http://shop.bytravel.cn/produce3/592783DC7CD5.html",
        #"http://shop.bytravel.cn/produce2/6CB395F49A748089706B70E7.html",
        #"http://shop.bytravel.cn/produce2/660C5E7383498393.html",
        #"http://shop.bytravel.cn/produce/5D07660E91D174DC/",
        #"http://shop.bytravel.cn/produce/index113.html",
        #"http://localhost/qunar_gugong.htm",
        #"http://localhost/qunar_tiananmen.htm",
    )

    # 抓取各个地区分页的特产 start,(不包含第一页)
    def parse_bak(self, response):
        hrefs = response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//div/b/a/@href').extract()
        for href in hrefs:
             arr = href.split(".")
             url = self.domain+arr[0]+"_list."+arr[1]
             yield scrapy.Request(url, callback=self.parse_page)

    def parse_page_bak(self, response):
        #由于scrapy的防重复机制，这样做会丢失对各分类下的第一页的抓取,可将parse中的回调函数名改为parse_item,跳过本函数
        nodes = response.xpath('//div[@class="f14b"]/a')
        if nodes:
            for node in nodes:
                url = self.domain+"/produce/"+node.xpath('@href').extract()[0]
                yield scrapy.Request(url, callback=self.parse_item)
                    
    def parse_item_bak(self, response):
        hrefs = response.xpath('//td[@id="bright"]/a/@href').extract()
        for href in hrefs:
            url = self.domain+href
            yield scrapy.Request(url, callback=self.parse_info)
    # 抓取各个地区分页的特产 end
            
            
    # 抓取各个地区推荐的特产 start
    def parse(self, response):
        hrefs = response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//div/b/a/@href').extract()
        for href in hrefs:
            url = self.domain+href
            yield scrapy.Request(url, callback=self.parse_page) 
            
    def parse_page(self, response):
        hrefs = response.xpath('//div[@id="tcjs"]/a/@href').extract()
        for href in hrefs:
            url = self.domain+href
            #print url
            yield scrapy.Request(url, callback=self.parse_info)        
    # 抓取各个地区推荐的特产 end
            

    def parse_info(self, response):
        item = BoyaItem()
        navNodes = response.xpath('//div[@id="page_left"]/div')[0].xpath('.//div/a/text()').extract()
        
        if len(navNodes)==1:
            item['pro'] = navNodes[0].encode('utf-8')
            item['city'] = ''
            item['county'] =  ''
        elif len(navNodes)==2:
            item['pro'] = navNodes[0].encode('utf-8')
            item['city'] = navNodes[1].encode('utf-8')
            item['county'] = ''
        elif len(navNodes)==3:
            item['pro'] = navNodes[0].encode('utf-8')
            item['city'] = navNodes[1].encode('utf-8')
            item['county'] = navNodes[2].encode('utf-8')

        titlep = response.xpath('//div[@id="page_left"]/div')[1].xpath('.//h1/text()').extract()
        if titlep:
            item['name'] = titlep[0].encode('utf-8')
        else:
            item['name'] = ''
            
        
        iconNode = response.xpath('//div[@id="page_left"]/div[@id="Layer1"]')
        if iconNode:

            picp = response.xpath('//div[@id="page_left"]/div')[6].xpath('.//a/img/@src').extract()
            if picp:
                item['pic'] = self.domain+picp[0].encode('utf-8')
            else:
                item['pic'] = ''
            
            introducep = response.xpath('//div[@id="page_left"]/div')[7].extract()
            if introducep:
                item['introduce'] = introducep.encode('utf-8')
            else:
                item['introduce'] = ''
                
            extp = response.xpath('//div[@id="page_left"]/div[@id="Layer1"]/div/img/@src').extract()
            item['ext'] = '|'.join(extp).encode('utf-8')
                
        else:
            
            picp = response.xpath('//div[@id="page_left"]/div')[5].xpath('.//a/img/@src').extract()
            if picp:
                item['pic'] = self.domain+picp[0].encode('utf-8')
            else:
                item['pic'] = ''
            
            introducep = response.xpath('//div[@id="page_left"]/div')[6].extract()
            if introducep:
                item['introduce'] = introducep.encode('utf-8')
            else:
                item['introduce'] = ''
                
            item['ext'] = ''
            
        #print item
        return item
'''��ע'''
# http://shop.bytravel.cn/ ���е�����a��ǩ
# response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//a')

# ����ʡ�ݵ�����  
# http://shop.bytravel.cn/produce/index141.html 
# ���� list �Ϳɵ��б�ҳ 
# http://shop.bytravel.cn/produce/index141_list.html
# response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//div/b/a/@href').extract()

# pageҳ��� 
# ��ҳ��Ϣ response.xpath('//div[@class="f14b"]/a')
# ����ҳ���� response.xpath('//td[@id="bright"]/a/@href').extract()

# ����ҳ
# ���� >>> response.xpath('//div[@id="page_left"]/div')[0].xpath('.//div/a/text()').extract() # [u'\u6e56\u5357', u'\u90b5\u9633', u'\u6b66\u5188\u7279\u4ea7']
# ���� >>> response.xpath('//div[@id="page_left"]/div')[1].xpath('.//h1/text()').extract()  # [u'\u6b66\u5188\u94dc\u9e45']
# ͼƬ >>> response.xpath('//div[@id="page_left"]/div')[6].xpath('.//a/img/@src').extract()  # [u'/images/head/2203.gif']
# ���� >>> response.xpath('//div[@id="page_left"]/div')[7].extract()
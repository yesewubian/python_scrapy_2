'''备注'''
# http://shop.bytravel.cn/ 所有地区的a标签
# response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//a')

# 所有省份的链接  
# http://shop.bytravel.cn/produce/index141.html 
# 加上 list 就可到列表页 
# http://shop.bytravel.cn/produce/index141_list.html
# response.xpath('//body/table')[1].xpath('tr/td')[0].xpath('div')[1].xpath('.//div/b/a/@href').extract()

# page页面的 
# 分页信息 response.xpath('//div[@class="f14b"]/a')
# 详情页链接 response.xpath('//td[@id="bright"]/a/@href').extract()

# 详情页
# 导航 >>> response.xpath('//div[@id="page_left"]/div')[0].xpath('.//div/a/text()').extract() # [u'\u6e56\u5357', u'\u90b5\u9633', u'\u6b66\u5188\u7279\u4ea7']
# 标题 >>> response.xpath('//div[@id="page_left"]/div')[1].xpath('.//h1/text()').extract()  # [u'\u6b66\u5188\u94dc\u9e45']
# 图片 >>> response.xpath('//div[@id="page_left"]/div')[6].xpath('.//a/img/@src').extract()  # [u'/images/head/2203.gif']
# 介绍 >>> response.xpath('//div[@id="page_left"]/div')[7].extract()
# import scrapy
# from scrapy.loader import ItemLoader
# from demo_scrapy_project.items import DemoScrapyProjectItem
#
# class QuotesSpider(scrapy.Spider):
#     name = "alibaba"
#
#     def __init__(self):
#         self.count = 1
#
#     def start_requests(self):
#         url = 'https://www.alibaba.com/products/shoes.html?IndexArea=product_en&page=1'
#         yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self,response):
#         shoes=response.selector.xpath('//h2[@class="title"]/a')
#         for shoe in shoes:
#             yield{
#                 "Title :":shoe.xpath('.//h2[@class="title"]/a/text()[1]').extract_first(),
#                 "Price :":shoe.xpath('.//div[@class="price"]/b/text()').extract_first(),
#                 "Minimum Pairs to Order :":shoe.xpath('.//div[@class="min-order"]/b//text()').extract_first()
#             }
#
#         if self.count <= 1:
#             self.count += 1
#             base_url="https://www.alibaba.com/products/shoes.html?IndexArea=product_en&page="
#             next_page_link=base_url+str(self.cnt)
#             print("**********************"+next_page_link)
#             yield scrapy.Request(url=next_page_link, callback=self.parse)
#
#
#

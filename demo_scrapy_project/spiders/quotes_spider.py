# import scrapy
# from scrapy.loader import ItemLoader
# from demo_scrapy_project.items import DemoScrapyProjectItem
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         url = 'https://www.goodreads.com/quotes?page=1'
#         yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self,response):
#         for quote in response.selector.xpath("//div[@class='quote']"):
#             loader=ItemLoader(item=DemoScrapyProjectItem(), selector=quote,response=response)
#             loader.add_xpath('Quote', ".//div[@class='quoteText']/text()[1]")
#             loader.add_xpath('Author', ".//div[@class='quoteText']/child::span")
#             loader.add_xpath('Tags',".//div[@class='greyText smallText left']/a")
#             yield loader.load_item()
#
#         next_pages= response.selector.xpath("//a[@class='next_page']/@href").extract()
#             # "/quotes?page=2"
#         if next_pages is not None:
#             base_url="https://www.goodreads.com"
#             for next_page in next_pages:
#                 next_page_link = base_url+next_page
#                 yield scrapy.Request(url=next_page_link, callback=self.parse)
#
#
#
#
#
#
# # yield{
# #                 'Quote : ':quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
# #                 'Author: ': quote.xpath(".//div[@class='quoteText']/span[@class='authorOrTitle']/text()").extract_first(),
# #                 'Tags : ':quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract_first()
# import scrapy
# from demo_scrapy_project.items import DemoScrapyProjectItem
#
# class QuotesSpider(scrapy.Spider):
#     name = "quotes_old"
#
#     def start_requests(self):
#         url = 'https://www.goodreads.com/quotes?page=1'
#         yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self,response):
#         for quote in response.selector.xpath("//div[@class='quote']"):
#             yield{
#                 'Quote : ':quote.xpath(".//div[@class='quoteText']/text()[1]").extract_first(),
#                 'Author: ': quote.xpath(".//div[@class='quoteText']/span[@class='authorOrTitle']/text()").extract_first(),
#                 'Tags : ':quote.xpath(".//div[@class='greyText smallText left']/a/text()").extract_first()
#
#             }
#         next_page = response.selector.xpath("//a[@class='next_page']/@href").extract_first()
#             # "/quotes?page=2"
#         if next_page is not None:
#             base_url="https://www.goodreads.com"
#             next_page_link = base_url+next_page
#             yield scrapy.Request(url=next_page_link, callback=self.parse)
#
#
#
#
#
#

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join
from w3lib.html import remove_tags

def remove_quotations(value):
    return value.replace(u"\u00a3",'')


class ItemsPYofBooks(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(str.strip,remove_tags),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_quotations,remove_tags),
        output_processor=TakeFirst()

    )
    stock = scrapy.Field(
        input_processor=MapCompose(str.strip,remove_tags),
        output_processor=TakeFirst()
    )
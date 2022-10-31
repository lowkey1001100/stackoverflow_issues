import scrapy

class Item(scrapy.Item):
    images_urls = scrapy.Field()
    images = scrapy.Field()


class ImagedownloaderItem(scrapy.Item):
    custom_settings = {
        "IMAGES_STORE" : "images",  # <- make sure whatever you put here is an existing empty folder at the top level of your project.
        "ITEM_PIPELINES" : {"scrapy.pipelines.images.ImagesPipeline": 1},
        "IMAGES_URLS_FIELD": "images_urls",
        "IMAGES_RESULT_FIELD": "images",
    }

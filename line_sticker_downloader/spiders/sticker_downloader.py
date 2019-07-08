# -*- coding: utf-8 -*-
import json
import scrapy


class StickerdownloaderSpider(scrapy.Spider):
    name = 'StickerDownloader'
    allowed_domains = ['https://store.line.me/stickershop/']
    start_urls = ['https://store.line.me/stickershop/product/1316911']

    def parse(self, response):
        ul = response.xpath('//ul[contains(@class, "FnStickerList")]')
        if ul:
            for li in ul.xpath('.//li[contains(@class, "FnStickerPreviewItem")]'):
                json_str = li.xpath('./@data-preview').get()
                data = json.loads(json_str, encoding='utf-8')
                image_url = data.get('staticUrl', None)
                if image_url:
                    yield {'image_urls': [image_url]}

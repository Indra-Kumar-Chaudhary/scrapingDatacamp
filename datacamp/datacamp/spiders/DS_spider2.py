# Datacamp course Links: parse Again

import scrapy 

class DCspider(scrapy.Spider):
    name='dcspider2'

    def start_requests(self):
        urls=['https://www.datacamp.com/courses/all']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self,response):
        links = response.css('div.course-block > a::attr(href)').extract()

        for link in links:
            yield response.follow(url=link, callback=self.parse2)

    def parse2(self,response):
        pass 
        # parse the course size here
# Datacamp course Links: save to File

import scrapy 

class DC_spider(scrapy.Spider):
    name ='dcspider'

    def start_request(self):
        urls=['https://www.datacamp.com/courses/all']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        links = response.css('div.course-block > a::attr(href)').extract()

        filepath = 'DC_links.csv'

        with open(filepath,'w') as f:
            f.writelines([link + '/n' for link in links])


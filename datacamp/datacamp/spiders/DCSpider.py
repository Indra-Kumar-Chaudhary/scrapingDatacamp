import scrapy

class DCSpider(scrapy.Spider):
    name='dc_spider'

    def start_request(self):
        urls=['https://wwww.datacamp.com/courses/all']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        # Simple example write out the html
        html_file='DC_courses.htm'

        with open(html_file,'wb') as fout:
            fout.write(response.body)

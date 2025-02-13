import scrapy
import os

class pubmed_spider(scrapy.Spider):
    name = "pubmed"
 
    start_urls = ['https://pubmed.ncbi.nlm.nih.gov/?term=((heart%20disease)%20AND%20((%222025%22%5BDate%20-%20Publication%5D%20%3A%20%223000%22%5BDate%20-%20Publication%5D)))%20AND%20(%22journal%20article%22%5BPublication%20Type%5D)&sort=']
    for i in range(2, 150):
        new_url = 'https://pubmed.ncbi.nlm.nih.gov/?term=((heart%20disease)%20AND%20((%222025%22%5BDate%20-%20Publication%5D%20%3A%20%223000%22%5BDate%20-%20Publication%5D)))%20AND%20(%22journal%20article%22%5BPublication%20Type%5D)&sort=&page='+str(i) + '#'
        start_urls.append(new_url)

    def parse(self, response):      
        base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        for articles in response.css('div.docsum-content'):
            yield {
                'id': articles.css('span.docsum-pmid::text').get(),
                'title': articles.css('a.docsum-title::text').get().strip(),
                'authors': articles.css('span.docsum-authors.full-authors::text').get(),
                'link': base_url+articles.css('a').attrib['href'],
                'journal_publication': articles.css('span.docsum-journal-citation.short-journal-citation::text').get().split('.')[0],
                'published_date': articles.css('span.docsum-journal-citation.full-journal-citation::text').get().split('.')[1].split(';')[0]                
            }
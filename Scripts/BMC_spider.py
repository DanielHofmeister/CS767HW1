import scrapy

class BMC_spider(scrapy.Spider):
    name = "bmc"
    start_urls = ['https://www.biomedcentral.com/search?searchType=publisherSearch&sort=PubDate&page=1&query=heart+disease']
    for i in range(2, 150):
        new_url = 'https://www.biomedcentral.com/search?searchType=publisherSearch&sort=PubDate&query=heart+disease&page=' + str(i)
        start_urls.append(new_url)

    def parse(self, response):    

        for articles in response.css('article.c-listing__content.u-mb-16'):
            yield {
                'id': articles.css('a[itemprop="url"]::attr(href)').get().split('/')[-1],
                'title': articles.css('h3[itemprop="name"] a::text').get(),
                'authors': articles.css('span.c-listing__authors-list::text').get(),
                'published_date': articles.css('span[itemprop="datePublished"]::text').get(),
                'journal_publication': articles.css('em[data-test="journal-title"]::text').get(),
                'link': articles.css('a[itemprop="url"]::attr(href)').get(),
                'article_type': articles.css('span[data-test="result-list"]::text').get(),
                'volume': articles.css('div[data-test="teaser-citation"] span:nth-of-type(2)::text').get().strip(),
                'issue':articles.css('div[data-test="teaser-citation"]::text').getall()[-1].strip()
            }
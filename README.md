# Crawler Templates

Crawler templates ease your crawling experience

## Parallel Crawler Example
```
urls = [
    {
        'id': 1,
        'url': 'https://google.com/'
    },
    {
        'id': 2,
        'url': 'https://facebook.com/'
    }
]
obj = ParallelCrawler()
def url_resolver(obj):
    return obj['url']
def callback(obj, content):
    print(f'CRAWLED: {content}')

obj.crawl(urls, url_resolver, callback)
```

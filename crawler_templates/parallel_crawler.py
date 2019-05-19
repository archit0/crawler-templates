import requests

from abc import ABC, abstractmethod
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor


TOTAL_CPUS = cpu_count()
TOTAL_PARALLEL = TOTAL_CPUS * 2
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


class ParallelCrawler:
    def __init__(self, total_workers=TOTAL_PARALLEL):
        self.total_workers = total_workers
        super().__init__()

    def get_source(self, inp):
        url, obj = inp
        return obj, requests.get(url, headers=HEADERS, allow_redirects=False).content

    def crawl(self, objects, resolve_url_from_obj_method, callback_method):

         with ThreadPoolExecutor(max_workers=self.total_workers) as executor:
            for obj, content in executor.map(
                self.get_source,
                [(resolve_url_from_obj_method(obj), obj) for obj in objects]
            ):
                callback_method(obj, content)

# coding=utf-8
import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        html_response = requests.get(url)
        if html_response.status_code != 200:
            print("网页爬取失败%s" % url)
            return None
        print(html_response.status_code)
        return html_response

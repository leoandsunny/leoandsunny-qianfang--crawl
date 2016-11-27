#  coding=utf-8

from qianfangkeji import html_downloader, html_parser, url_manager, outputer
root_url = "http://guba.eastmoney.com/list,002373_1.html"

class CrawlMain(object):

    def __init__(self):
        self.urls = url_manager.urlmanager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.htmlparser()
        self.out = outputer.output()
        self.root_info = []
        self.info_url = []
        self.texts = []
        self.comments = []

    def CrawRoot_url(self, root_url):
        self.urls.get_root_urls(root_url)  # 得到所有根节点，下一步下载所有根节点
        count = 0
        while self.urls.has_new_url(self.urls.root_new_urls):
            count += 1
            get_root_url = self.urls.get_new_root_url()
            root_html_response = self.downloader.download(get_root_url)
            print('下载第%d个root_url成功' % count)
            root_info = self.parser.get_root_infos(root_html_response)
            info_url = self.parser.get_info_url(root_html_response)
            self.root_info.extend(root_info)
            self.info_url.extend(info_url)

        print(len(self.root_info), '\n', len(self.info_url))
        print(self.info_url[7:9])
        print(self.root_info[7:9])


if __name__ == "__main__":
    crawl = CrawlMain()
    crawl.CrawRoot_url(root_url)
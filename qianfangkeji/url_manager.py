# coding=utf-8
class urlmanager(object):
    def __init__(self):
        self.root_new_urls = set()
        self.root_old_urls = set()
        self.info_new_urls = set()
        self.info_old_urls = set()
        self.comment_new_urls = set()
        self.comment_old_urls = set()

    def get_root_urls(self, url):
        for i in range(0, 2):
            self.root_new_urls.add('http://guba.eastmoney.com/list,002373_'+str(i)+'.html')
        return self.root_new_urls

    def has_new_url(self, urls):
        return len(urls) != 0

    def get_new_root_url(self):
        get_root_url = self.root_new_urls.pop()
        self.root_old_urls.add(get_root_url)
        return get_root_url




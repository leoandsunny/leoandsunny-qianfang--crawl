# coding=utf-8
import re
from bs4 import BeautifulSoup


class htmlparser(object):
    # 得到根页面上的信息，比如阅读量、评论数、标题、作者、发表日期、更新日期
    def get_root_infos(self,root_html_response):
        root_info = []  # 每个root_page的信息,阅读量、评论数、标题、作者、发表日期、更新日期
        soup = BeautifulSoup(root_html_response.text,'html.parser')
        for l in soup.select('div.articleh'):
            a = []
            for m in range(1, 7):
                a.append(l.select_one('span.l' + str(m)).get_text())
            root_info.append(a)
        return root_info

    # 得到评论详情页的链接
    def get_info_url(self, html_response):
        info_url = []
        pat = re.compile('<div class="articleh">.*?<a href="(.*?)".*?</span>', re.S)
        url = re.findall(pat, html_response.text)
        for i in range(0, len(url)):
            if r'/' not in url[i]:
                b = 'http://guba.eastmoney.com/' + url[i]
            else:
                b = 'http://guba.eastmoney.com' + url[i]
            info_url.append(b)
        return info_url  # info_url的网址链接

    # 详情页解析
    def get_info_comments_url(self, html_response):
        # 找到详情页的评论链接
        soup = BeautifulSoup(html_response.text, 'html.parser')
        info_comments_url = []
        page = soup.select_one('span.sumpage').get_text()
        if page is None:
            page == 1
        else:
            pass
        return info_comments_url

    def get_info_texts(self, html_response):  # 获取文本内容texts
        texts = []
        soup = BeautifulSoup(html_response.text, 'html.parser')
        # 获取文章内容
        txt = soup.select('div.stockcodec')
        for tex in txt:
            texts.append(tex.get_text())

    def get_info_comments(self, html_response):
        # 获取文章评论【用户、评论内容】
        comments = []
        soup = BeautifulSoup(html_response.text, 'html.parser')
        username = soup.select('div.zwlianame')
        comment = soup.select('div.zwlitext stockcodec')
        for num in range(0, len(username)):
            a = username[num].get_text()
            b = comment[num].get_text()
            if len(b) == 0:
                b = 'None'
            lis = [a, b]
            comments.append(lis)
            # 获取详情页的所有评论

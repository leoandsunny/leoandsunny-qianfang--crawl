#  coding=utf-8
import pandas as pd
class output(object):
    def __init__(self):
        self.root_datas = []
        self.info_datas = []

    def outputdata(self,root_info):
        root_info_DF = pd.DataFrame(root_info,
                                    columns=['read_num', 'comment_num', 'titles',
                                             'author', "update_time", "pub_time"])
        return root_info_DF
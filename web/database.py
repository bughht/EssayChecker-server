from re import X
from tkinter.tix import COLUMN
import pandas as pd
import random

    def __init__(self):
        self.data_source = '/web/database/data.csv' 
        self.data_frame = self.load_data()  
 
 
    def load_data(self):
        df = pd.read_csv(self.data_source)
        return df
 
    def save_data(self):
        self.data_frame.to_csv(self.data_source, encoding='utf-8', index=False)
 
    def filter(self, type, key):
        result = None
        if type == 1:
            result = self.data_frame.query('Topic.str.contains("{}", na=False)'.format(key))
        if type == 2:
            result = self.data_frame.query('Essay.str.contains("{}", na=False)'.format(key))
        if type == 3:
            result = self.data_frame.query('Mark_Content.str.contains("{}", na=False)'.format(key))
        if type == 4:
            result = self.data_frame.query('Comment_Content.str.contains("{}", na=False)'.format(key))
        if type == 5:
            result = self.data_frame.query('Mark_Statement.str.contains("{}", na=False)'.format(key))
        if type == 6:
            result = self.data_frame.query('Comment_Statement.str.contains("{}", na=False)'.format(key))
        if type == 7:
            result = self.data_frame.query('Mark_Organization.str.contains("{}", na=False)'.format(key))
        if type == 8:
            result = self.data_frame.query('Comment_Organization.str.contains("{}", na=False)'.format(key))
        if type == 9:
            result = self.data_frame.query('Mark_Readability.str.contains("{}", na=False)'.format(key))
        if type == 10:
            result = self.data_frame.query('Comment_Readability.str.contains("{}", na=False)'.format(key))
        if type == 11:
            result = self.data_frame.query('Mark_Grammar.str.contains("{}", na=False)'.format(key))
        if type == 12:
            result = self.data_frame.query('Comment_Grammar.str.contains("{}", na=False)'.format(key))
        if type == 13:
            result = self.data_frame.query('Mark_Overall.str.contains("{}", na=False)'.format(key))
        if type == 14:
            result = self.data_frame.query('Comment_Overall.str.contains("{}", na=False)'.format(key))
        self.format_print(result)
 


# 保存json数据 (简单数据)
df.to_json('.json')

print(data.head(x))


def Fun_outputCSV(_filename,_list_r):
    with open(_filename,'a+') as obj_f:
        for str_re in _list_r:
            obj_f.write(str_re+'\n')

import
df=pd.Dataframe(columns=)
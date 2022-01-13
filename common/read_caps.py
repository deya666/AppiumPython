# -*- coding:utf-8 -*-
# @Time   : 2021-12-11 19:30
# @Author : DingYa

import yaml
import os

# 获取当前文件的上一层路径
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
caps_path = os.path.join(os.path.join(cur_path,'config'),'waiqin_caps.yaml')

def read_caps():
    with open(caps_path,'r',encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data




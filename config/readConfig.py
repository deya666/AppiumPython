# -*- coding:utf-8 -*-
# @Time   : 2021-12-11 19:30
# @Author : DingYa

import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))

configPath = os.path.join(cur_path,'email.cfg')

conf = configparser.ConfigParser()
conf.read(configPath,encoding='utf-8')

smtp_server = conf.get("email","smtp_server")

sender = conf.get("email","sender")

psw = conf.get("email", "psw")

receiver = conf.get("email", "receiver").split(',')

port = conf.get("email", "port")

subject = conf.get("email","subject")

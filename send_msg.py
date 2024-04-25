# -*- coding:utf8 -*-
"""
@ Author: wjlv4
@ File: send_msg.py
@ Time: 2024/4/25
@ Contact: wenju_lv@163.com
@ Desc: 
"""

import config
import requests
from datetime import datetime


# 消息推送
def send_msg(title, content):
    if config.PUSH_TOKEN is None:
        return
    url = 'http://www.pushplus.plus/send'
    r = requests.get(url, params={'token': config.PUSH_TOKEN,
                                  'title': title,
                                  'content': content})
    print(f'通知推送结果：{r.status_code, r.text}')


if __name__ == '__main__':
    send_msg('测试时间', '现在的时间是' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

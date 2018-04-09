#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: anzhang28@163.com
# FileName: media_libs.py
# Function: media operation method/class
# Date: 2018/03/08

import re
import os
import requests


# check whether the url is a hls url or not
def is_hls_url(url):
    pattern = re.compile('(.*?)://(.*/)(.*?)/(.*?)\.')
    match_res = re.match(pattern, url)
    if match_res:
        return match_res
    else:
        return False


# get the protocol,stream_name,path information from the url
def analysis_url(url):
    hls_tag = is_hls_url(url)
    if hls_tag:
        match_res = hls_tag.groups()
        url_info = {}
        url_info['protol'] = match_res[0]
        if match_res[3] == 'index':
            url_info['name'] = match_res[2]
            url_info['path'] = match_res[1]
        else:
            url_info['name'] = match_res[3]
            url_info['path'] = match_res[1] + match_res[2] + '/'
        return url_info
    else:
        return False


class M3U8:
    def __init__(self, url):
        self.url = url
        self.url_info = analysis_url(url)
        self.content = requests.get(url).content.decode('utf-8')

    def ts_list(self):
        ts_pattern = re.compile('#EXTINF:(.*?)\n(.*?)\n')
        ts_list = re.findall(ts_pattern, self.content)
        return ts_list

    def m3u8_download(self, store_path=os.getcwd()):
        if is_hls_url(self.url):
            store_path = os.path.join(store_path, self.url_info['name'])
            if not os.path.exists(store_path):
                os.makedirs(store_path)
            with open(os.path.join(store_path, 'index.m3u8'), 'wb') as media:
                media.write(requests.get(self.url).content)
        else:
            raise Exception('Ivalid m3u8', self.url)

    def ts_download(self, store_path=os.getcwd()):
        store_path = os.path.join(store_path, self.url_info['name'])
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        for t, ts in self.ts_list():
            if not is_hls_url(ts):
                # ts_name = os.sep.join(ts.split('/')) + '.ts'
                ts += self.url_info['path']
            # else:
                # ts_name = analysis_url(ts)['name'] + '.ts'
            ts_name = re.search('.*/([^/]+\.ts)', ts).group(1)
            with open(os.path.join(store_path, ts_name), 'wb') as media:
                media.write(requests.get(ts).content)

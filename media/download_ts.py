#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: anzhang28@163.com
# FileName: download_ts.py
# Function: download the m3u8 file and its ts file
# Date: 2018/03/08

import os
import sys
sys.path.append('..')
os.chdir(sys.path[0])
import test_libs.media_libs as media_libs

if __name__ == '__main__':
    m3u8_url = 'http://hls.fastmedia.com.cn/audio/aac/index.m3u8'
    store_path = 'E:\\media\\download'
    hls_h264 = media_libs.M3U8(m3u8_url)
    hls_h264.m3u8_download(store_path)
    hls_h264.ts_download(store_path)

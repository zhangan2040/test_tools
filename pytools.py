#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: anzhang28@163.com
# Filename: pytools.py
# Date: 2019/03/01
# Description: 测试中用到的小工具


import tkinter as tk
import time


class DateTrans():
    def __init__(self):
        self.dt = tk.Tk()
        self.dt.title('Time-Stamp tools by Python(zhangan)')
        self.date = tk.StringVar()
        self.date.set(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
        self.stamp = tk.StringVar()
        self.stamp.set(time.time())
        self.create_widgets()

    def create_widgets(self):
        self.date2stamp = tk.LabelFrame(self.dt, text='时间戳转换工具：', height=10, width=200)
        self.date2stamp.grid()
        self.lf_date_label = tk.Label(self.date2stamp, text='日期：')
        self.lf_date_label.grid(row=0, column=0, ipadx=10, ipady=5)
        self.lf_date_label = tk.Label(self.date2stamp, text='时间戳：')
        self.lf_date_label.grid(row=0, column=2, ipadx=10, ipady=5)
        # 用于显示日期
        self.lf_date_entry = tk.Entry(self.date2stamp, textvariable=self.date)
        self.lf_date_entry.grid(row=0, column=1, sticky=tk.W, padx=10)
        # 用于显示时间戳
        self.lf_stamp_entry = tk.Entry(self.date2stamp, textvariable=self.stamp)
        self.lf_stamp_entry.grid(row=0, column=3, sticky=tk.W, padx=10)
        # 添加转换按钮
        self.s2d_button = tk.Button(self.date2stamp, text='<<', command=self.stamp_date)
        self.s2d_button.grid(row=1, column=1, ipadx=10)
        self.d2s_button = tk.Button(self.date2stamp,text='>>', command=self.date_stamp)
        self.d2s_button.grid(row=1, column = 3, ipadx=10)

    def date_stamp(self):
        cur_time = time.strptime(self.lf_date_entry.get(), '%Y/%m/%d %H:%M:%S')
        self.stamp.set(time.mktime(cur_time))

    def stamp_date(self):
        cur_time = time.localtime(float(self.lf_stamp_entry.get()))
        self.date.set(time.strftime('%Y/%m/%d %H:%M:%S', cur_time))

if __name__ == '__main__':
    trans_date_app = DateTrans()
    trans_date_app.dt.mainloop()

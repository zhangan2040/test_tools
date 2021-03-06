#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: anzhang28@163.com
# Filename: pytools.py
# Date: 2019/03/01
# Description: 测试中用到的小工具


import tkinter as tk
import time
import base64


class SoulTools(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid()
        self.title('SoulTools by python(zhangan)')
        self.create_menu()
        self.bs_view, self.ds_view = False, False

    def create_menu(self):
        self.ds_button = tk.Button(self, text='时间戳转换', command=self.switch_ds)
        self.ds_button.grid(row=0, column=0, sticky=tk.N+tk.E+tk.W)
        self.bs_button = tk.Button(self, text='Base64工具', command=self.switch_bs)
        self.bs_button.grid(row=0, column=1, sticky=tk.N + tk.E + tk.W)
        self.main_lf = tk.LabelFrame(self, height=500, width=800)
        self.main_lf.grid(row=1, column=0, columnspan=15)

    def switch_ds(self):
        if self.bs_view:
            self.main_lf.destroy()
            self.main_lf = tk.LabelFrame(self, height=500, width=800)
            self.main_lf.grid(row=1, column=0, columnspan=15)
            self.bs_view = False
        self.date_var = tk.StringVar()
        self.date_var.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.stamp_var = tk.StringVar()
        self.stamp_var.set(int(time.time()))
        # 添加时间输入框
        self.date_label = tk.Label(self.main_lf, text='日期：')
        self.date_label.grid(row=0, column=0, ipadx=10)
        self.date_entry = tk.Entry(self.main_lf, textvariable=self.date_var)
        self.date_entry.grid(row=0, column=1)
        self.stamp_label = tk.Label(self.main_lf, text='时间戳：')
        self.stamp_label.grid(row=0, column=2, ipadx=10)
        self.stamp_entry = tk.Entry(self.main_lf, textvariable=self.stamp_var)
        self.stamp_entry.grid(row=0, column=3, padx=10)
        # 添加操作button
        self.s2d_button = tk.Button(self.main_lf, text='<<', command=self.stamp_date)
        self.s2d_button.grid(row=1, column=1, ipadx=10, pady=20)
        self.d2s_button = tk.Button(self.main_lf, text='>>', command=self.date_stamp)
        self.d2s_button.grid(row=1, column=3, ipadx=10, pady=20)
        self.ds_view = True

    def switch_bs(self):
        if self.ds_view:
            self.main_lf.destroy()
            self.main_lf = tk.LabelFrame(self, height=500, width=800)
            self.main_lf.grid(row=1, column=0, columnspan=15)
            self.ds_view = False
        self.string_var = tk.StringVar()
        self.code_var = tk.StringVar()
        # 添加编/解码字符输入框
        self.string_label = tk.Label(self.main_lf, text='原始字符：')
        self.string_label.grid(row=0, column=0, ipadx=10, sticky=tk.N)
        self.string_text = tk.Text(self.main_lf)
        self.string_text.grid(row=0, column=1)
        self.code_label = tk.Label(self.main_lf, text='转码字符：')
        self.code_label.grid(row=0, column=6, ipadx=10, sticky=tk.N)
        self.code_text = tk.Text(self.main_lf)
        self.code_text.grid(row=0, column=7)
        # 添加操作button
        self.s2d_button = tk.Button(self.main_lf, text='转码', command=self.bs_codec)
        self.s2d_button.grid(row=1, column=1, ipadx=30, pady=20)
        self.d2s_button = tk.Button(self.main_lf, text='解码', command=self.bs_encodec)
        self.d2s_button.grid(row=1, column=7, ipadx=30, pady=20)
        self.bs_view = True

    def date_stamp(self):
        cur_time = time.strptime(self.date_entry.get(), '%Y-%m-%d %H:%M:%S')
        self.stamp_var.set(int(time.mktime(cur_time)))

    def stamp_date(self):
        cur_time = time.localtime(int(self.stamp_entry.get()[:10]))
        self.date_var.set(time.strftime('%Y-%m-%d %H:%M:%S', cur_time))

    def bs_codec(self):
        decode_bstring = self.string_text.get('1.0', tk.END).encode(encoding='utf-8')
        encode_str = base64.b64encode(decode_bstring)
        self.code_text.delete('1.0', tk.END)
        self.code_text.insert(tk.INSERT, encode_str.decode(encoding='utf-8'))

    def bs_encodec(self):
        encode_str = self.code_text.get('1.0', tk.END).encode(encoding='utf-8')
        decode_bstring =base64.b64decode(encode_str)
        self.string_text.delete('1.0', tk.END)
        self.string_text.insert(tk.INSERT, decode_bstring.decode(encoding='utf-8'))



if __name__ == '__main__':
    app = SoulTools()
    app.mainloop()


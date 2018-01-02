# coding:utf8
"""
--------------------------------------------------------------------------
    File:   common.py
    Auth:   zsdostar
    Date:   2018/1/2 16:58
    Sys:    Windows 10
--------------------------------------------------------------------------
    Desc:   
--------------------------------------------------------------------------
"""
__author__ = 'zsdostar'
import hashlib

def get_md5(url):
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print get_md5("http://www.jobbole.com")
'''表明对外开放的只有"hello"这个字符串，想要使用all则需要在其文件内
声明from tesiting import *
'''
__all__ =["hello"]

hello = "hello demo2"

def f():
    print("demo2.py f()")

class Demo2:
    pass
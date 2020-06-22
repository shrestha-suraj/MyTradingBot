import threading

def printData():
    print("Hello World")

def set_interval(funct,interval):
    def func_wrapper():
        set_interval(funct,interval)
        funct()
    t=threading.Timer(interval,func_wrapper)
    t.start()
    return t

set_interval(printData,3);
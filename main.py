import requests, json, time
from datetime import datetime

def local2utc(stime):
    #utc timezone to loacal zone
    #有些服务端时间点用utc
    dt = datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")
    mtime = dt.timestamp()
    mtime -= 8*3600
    ret = datetime.fromtimestamp(mtime)
    return str(ret)       
       

if __name__ == "__main__":

    print(local2utc('2018-10-12 00:00:00'))
    print(local2utc('2018-10-23 21:00:00'))  
    
  


    





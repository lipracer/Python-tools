import sys, os
import requests, json, time
from datetime import datetime

import re

def local2utc(stime):
    #utc timezone to loacal zone
    #有些服务端时间点用utc
    dt = datetime.strptime(stime, "%Y-%m-%d %H:%M:%S")
    mtime = dt.timestamp()
    mtime -= 8*3600
    ret = datetime.fromtimestamp(mtime)
    return str(ret)

class ReplaceAll(object):
    '''
    _xx protected
    __xx private
    '''
    def __init__(self, path, word):
        #self转为父类对象
        super(ReplaceAll, self).__init__()
        self._path = path
        self._word = word
        self.__info = "LL"#real name self._ReplaceAll__info
        self._all_files = []
    def find_all_file(self):
        def find_file(path):
            if os.path.isfile(path):
                self._all_files.append(path)
                return
            elif os.path.isdir(path):
                for it in os.listdir(path):
                    find_file(os.path.join(path, it))
        find_file(self._path)

        def chack_file(filename):
            with open(filename, "rb") as f:
                content = f.read().decode('utf-8', errors='ignore')
                group = re.search(self._word, content)
                if group:
                    print(filename, ":", group[0])
                
                return group
        self._all_files = filter(chack_file, self._all_files)
        for i in self._all_files:
            print(i)
        pass
        
        
       

if __name__ == "__main__":

    print(local2utc('2018-10-12 00:00:00'))
    print(local2utc('2018-10-23 21:00:00'))  
    replace = ReplaceAll('../LLLog', 'PZLog')
    replace.find_all_file()

  


    





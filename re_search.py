import sys, os
import requests, json, time
from datetime import datetime

import re
import socket

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

        def check_file(filename):
            file_type = ['.h', '.cpp', '.hpp', '.m', '.mm', '.cc']
            for it in file_type:
                if filename.endswith(it):
                    with open(filename, "rb") as f:
                        content = f.read().decode('utf-8', errors='ignore')
                        group = re.search(self._word, content)             
                        return group
            
                    

        self._all_files = list(filter(check_file, self._all_files))

        for i in self._all_files:
            print(i)


    def __iter__(self):
        print("__iter__")
        self.tmp_it = iter(self._all_files)
        return self            
        pass
    def __next__(self):
        print("__next__")
        fn = next(self.tmp_it)

        new_content = ''
        with open(fn, "rb") as f:
            content = f.read().decode('utf-8', errors='ignore')
            def sub_replace(mobj):  
                return "LL" + mobj[2]
            new_content = re.sub(self._word, sub_replace, content)

        with open(fn, "wt") as f:
            f.write(new_content)
        return fn  
       

if __name__ == "__main__":                                           
    '''
    replace = ReplaceAll('../../first/LLLog', '()(\w+)')
    replace.find_all_file()
    '''
    
    #print(os.path.dirname(os.path.abspath(__file__)))

    '''
    for i in replace:
        print(i)
        input()
    '''


  


    





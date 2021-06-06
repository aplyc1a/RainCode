#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-06
# @Author  : aplyc1a
# @FileName: db2json.py
import optparse
import json
import re

if __name__ == '__main__':
    parser = optparse.OptionParser('')
    parser.add_option('-i', '--input', dest = 'input_file', type = 'string',  help = '待转化文件')
    parser.add_option('-n', '--keyname', dest = 'key_name', type = 'string',  help = '类型名')
    (options,args) = parser.parse_args()

    fp = open(options.input_file,'r')
    count=0
    print("{\r\n\t\"%s\":{\r\n" %(options.key_name), end="")
    for line in fp.readlines():
        if count:
            print(",")
        line = line.strip('\r').strip('\n')
        print("\t\t\"%s\":\"%s\"" %(str(count),line), end="")
        count+=1
    print("\r\n\t}\r\n}")

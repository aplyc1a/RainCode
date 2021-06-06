#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-05-29
# @Author  : aplyc1a
# @FileName: raincode.py
import optparse
import json
import re

class target:
    name=[]
    birth=[]
    phone=[]
    sfz=[]
    qq=[]
    splitcode=[]
    word=[]
    filling=[]
    common=[]
    number=[]

    def __init__(self, configuration_file):
        self.set_information(configuration_file)
        
    def set_feature(self, data):
        l=['name','birth','phone','sfz','qq','splitcode','word','filling','number']
        for i in l:
            if i in data.keys():
                for j in data[i].keys():
                    if data[i][j]:
                        self.get_feature_by_name(i).append(data[i][j])

    def set_information(self, config_file):
        try:
            f = open(config_file, "r")
            data = json.load(f)
        except Exception as e:
            print("[Error] 配置文件加载失败.%s" %e)
            exit(0)

        self.set_feature(data)
    def get_feature_by_name(self, feature_name):
        return getattr(self,feature_name)

def raindrops(units,cursor,model):
    if cursor >= len(units):
        if store_btn:
            fp_store.writelines(model+"\n")
        else :
            print(model)
        return
        
    if units[cursor]=='number':
        for j in t.get_feature_by_name(units[cursor]):
            if '-' in j:
                a,b= j.split('-')
                for k in range(int(a),int(b)+1):
                    raindrops(units,cursor+1,model.replace('%<'+units[cursor]+'>%',str(k),1))
            else:
                for j in t.get_feature_by_name(units[cursor]):
                    raindrops(units,cursor+1,model.replace('%<'+units[cursor]+'>%',j,1))
    else :
        for j in t.get_feature_by_name(units[cursor]):
            raindrops(units,cursor+1,model.replace('%<'+units[cursor]+'>%',j,1))

if __name__ == '__main__':
    parser = optparse.OptionParser('')
    parser.add_option('-j', '--json', dest = 'config_file', type = 'string', default="config.json", help = '加载配置文件')
    parser.add_option('-m', '--model', dest = 'template_file', type = 'string', default="model/big.model", help = '加载模板文件')
    parser.add_option('-o', '--output', dest = 'output_file', type = 'string', help = '输出文件')
    parser.add_option('-i', '--import', dest = 'import_file', type = 'string', help = '加载自定义弱口令字典')
    parser.add_option('-e', '--evolving', dest = 'fuzz_btn', action="store_true", default=False, help = '变异模式，@todo')
    parser.add_option('-v', '--verbose', dest="verbose", action="store_true", default=False, help="详细模式")
    (options,args) = parser.parse_args()

    t = target(options.config_file)
    fp_tmplt = open(options.template_file,'r')
    store_btn=0
    if options.output_file:
        fp_store = open(options.output_file,'a')
        store_btn = 1

    if options.import_file:
        fp_common = open(options.import_file,'r')
        if store_btn:
            for i in fp_common.readlines():
                fp_store.writelines(i.strip('\r'))
        else :
            for i in fp_common.readlines():
                print(i.strip('\r').strip('\n'))
        fp_common.close()

    for model in fp_tmplt.readlines():
        model = model.strip('\r').strip('\n')
        if options.verbose:
            print("[Debug] model:",model)
        v = model
        p = re.compile(r'\%\<(\w+)\>\%')
        u = p.findall(model)
        i = 0
        raindrops(u,i,v)

    if options.output_file:
        fp_store.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-05-29
# @Author  : aplyc1a
# @FileName: raincode.py
import optparse
import json
import pprint

class human:
    name=[]
    birth=[]
    phone=[]
    sfz=[]
    splitcode=[]
    filling=[]
    common=[]
    highrisk_dic={}

    def __init__(self, configuration_file):
        self.set_information(configuration_file)
        
    def set_feature(self, data):
        for i in data['name'].keys():
            if data['name'][i]:
                self.name.append(data['name'][i])

        for i in data['birth'].keys():
            if data['birth'][i]:
                self.birth.append(data['birth'][i])
                
        for i in data['phone'].keys():
            if data['phone'][i]:
                self.phone.append(data['phone'][i])

        for i in data['sfz'].keys():
            if data['sfz'][i]:
                self.sfz.append(data['sfz'][i])

        for i in data['splitcode'].keys():
            if data['splitcode'][i]:
                self.splitcode.append(data['splitcode'][i])

        for i in data['filling'].keys():
            if data['filling'][i]:
                self.filling.append(data['filling'][i])

        for i in data['common'].keys():
            if data['common'][i]:
                self.common.append(data['common'][i])

    def set_information(self, config_file):
        try:
            f = open(config_file, "r")
            data = json.load(f)
        except:
            print("[Error] 配置文件加载失败")
            exit(0)

        self.set_feature(data)
        #print(self.name)
    def get_feature_by_name(self, feature_name):
        return getattr(self,feature_name)

def raindrops(units,cursor,model):
    if cursor >= len(units):
        if store_btn:
            fp_store.writelines(model+"\n")
        else :
            print(model)
        return
    for j in man.get_feature_by_name(units[cursor]):
        #print(model.replace('%'+units[cursor]+'%',j))
        raindrops(units,cursor+1,model.replace('%'+units[cursor]+'%',j))

if __name__ == '__main__':
    parser = optparse.OptionParser('')
    parser.add_option('-j', '--json', dest = 'config_file', type = 'string', default="config.json", help = '加载配置文件')
    parser.add_option('-m', '--model', dest = 'template_file', type = 'string', default="model/big.model", help = '加载模板文件')
    parser.add_option('-o', '--output', dest = 'output_file', type = 'string', help = '输出文件')
    parser.add_option('-i', '--import', dest = 'import_btn', action="store_true", default=False, help = '加载自定义弱口令字典')
    parser.add_option('-s', '--smart', dest = 'smart_btn', action="store_true", default=False, help = '智能模式，@todo')
    parser.add_option('-a', '--all', dest = 'all_btn', action="store_true", default=False, help = '全量模式，@todo')
    parser.add_option('-e', '--evolving', dest = 'fuzz_btn', action="store_true", default=False, help = '变异模式，@todo')
    parser.add_option('-v', '--verbose', dest="verbose", action="store_true", default=False, help="详细模式")
    (options,args) = parser.parse_args()

    man = human(options.config_file)
    fp_tmplt = open(options.template_file,'r')
    store_btn=0
    if options.output_file:
        fp_store = open(options.output_file,'a')
        store_btn = 1

    if options.import_btn:
        fp_common = open("db/common.txt",'r')
        if store_btn:
            for i in fp_common.readlines():
                fp_store.writelines(i.strip('\r'))
        else :
            for i in fp_common.readlines():
                print(i.strip('\r').strip('\n'))
        fp_common.close()

    for model in fp_tmplt.readlines():# 不同的模型
        model = model.strip('\r').strip('\n')
        v = model
        u = [i for i in model.split('%') if i !='']
        u = list(set(u)) # u表示所有待替换的特征名
        # man.get_feature_by_name(u) #表示对应特征的所有可能的值
        i = 0
        raindrops(u,i,v)

    if options.output_file:
        fp_store.close()
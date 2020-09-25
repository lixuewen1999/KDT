# coding=gbk
'''
@author: lixuewen
@file: common.py
@time: 2020/9/20 18:04
@desc:
'''

from selenium import webdriver
import time
class KDT():
    def __init__(self):
        self.driver = None

    def open(self,url,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.get(url)

    def wait(self,timeout,*args):
        time.sleep(int(timeout))

    def input(self,identify,value):
        self.find_element(identify).clear()
        self.find_element(identify).send_keys(value)

    def click(self,identify):
        self.find_element(identify).click()

    def check_exist(self,identify,name):
        try:
            self.find_element(identify)
            print('{}测试通过，{},元素存在'.format(name,identify))
        except:
            print('{}测试失败，{},元素不存在'.format(name,identify))

    def check_value(self,identify,expect,name):
        try:
            actual = self.find_element(identify).text
            if actual == expect:
                print('{}测试通过，{}元素值预期{}，实际{}'.format(name,identify,expect,actual))
            else:
                print('{}测试失败,{}元素值预期{}，实际{}'.format(name,identify,expect,actual))
        except:
            print('{}找不元素{}，测试失败'.format(name,identify))



    def find_element(self,identify):
        how = identify.split('=',1)[0]
        what = identify.split('=',1)[1]
        if how == 'id':
            return self.driver.find_element_by_id(what)
        elif how == 'xpath':
            return self.driver.find_element_by_xpath(what)

    def start(self):
        with open('../keyword/login.txt',encoding='utf-8') as file:
            line_list = file.readlines()
        name = ''
        for line in line_list:
            if line.startswith('#'):
                name = line.strip().replace('# ','')
                continue
            key_list = line.strip().split(',')
            operation = key_list[0]
            operation = operation.replace(' ','_')
            # print(operation)
            args = []
            for i in range(1,len(key_list)):
                args.append(key_list[i])
            if operation.startswith('check'):
                args.append(name)
                getattr(self,operation)(*args)
            else:
                getattr(self,operation)(*args)

if __name__ == '__main__':
    KDT().start()
    # with open('../keyword/login.txt',encoding='gbk') as file:
    #     line_list = file.readlines()
    # print(line_list)

# coding:utf-8
from selenium import webdriver
import time
from optparse import OptionParser

def login_weibo(user,pwd,weibo):
    weibo.get('http://weibo.com/login.php')
    time.sleep(5)
    # send username
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # send password
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pwd)
    # not save state
    weibo.find_element_by_xpath('//*[@id="login_form_savestate"]').click()
    # click login button
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    time.sleep(5)
    print '[debug] login success'

def open_weibo(weibo):
    weibo.get('http://weibo.com/')
    time.sleep(5)
    
def delete_weibo(user,pwd,num,weibo):
    login_weibo(user,pwd,weibo)
    scroll_height_js = 'document.documentElement.scrollTop=200'
    time.sleep(3)
    weibo.find_element_by_xpath('//*[@id="v6_pl_rightmod_myinfo"]/div/div/div[2]/ul/li[3]/a/strong').click()
    while True:
        del_ = raw_input('continue delete or quit?(c/q)')
        # del_=0
        weibo.refresh()
        if del_ == 'c':
        # delete
            time.sleep(2)
            for i in range(0,num):
                # time.sleep(3)
                weibo.execute_script(scroll_height_js)
                time.sleep(3)
                weibo.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/a/i').click()
                weibo.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a').click()
                weibo.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/div[2]/div/p[2]/a[1]/span').click()
        else:
            break
    
def start_weibo():

    parser = OptionParser()
    parser.add_option("-u", "--usr", default = False, help = "your username of weibo")
    parser.add_option("-p", "--pwd", default = False, help = "your password of weibo")
    parser.add_option("-n", "--num", type = 'int' ,default = False, help = "the number to delete at once. default num is 10.")
    (options, args) = parser.parse_args()
    
    if options.usr:
        usr_ = options.usr
    else:
        print "[warning] please input your username."
        
    if options.pwd:
        pwd_ = options.pwd
    else:
        print "[warning] please input your username."
        
    if options.num:
        num_ = options.num
    else:
        num_ = 10
        
    
    if options.usr and options.pwd:
        weibo = webdriver.Firefox()
        weibo.maximize_window()
        time.sleep(10)
        
        delete_weibo(usr_,pwd_,num_,weibo)
        weibo.close()
    
if __name__ == '__main__':
    start_weibo()
    
    

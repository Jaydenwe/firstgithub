#!/usr/bin/env python
#coding=utf8

""" Simulate a user login to Sina Weibo with cookie.
You can use this method to visit any page that requires login.
"""
import urllib2
import re
import sys
import json
import time,random
import MySQLdb
from bs4 import BeautifulSoup
type = sys.getfilesystemencoding()

# ALL_NAMES = ["姚晨","陈坤","赵薇","郭德纲","林心如","谢娜","何炅","林志颖","王力宏","angelababy","范玮琪","韩庚","杨幂","高圆圆","吴奇隆","马伊琍","小S","刘亦菲","蔡依林","陈乔恩","唐嫣","胡歌","张靓颖","黄晓明","张杰","李敏镐","成龙","王菲","张智霖","范冰冰","钟欣桐","张翰","陆毅","柳岩","郭采洁","五月天阿信","李晨","孙俪","周笔畅","陈建州","蔡卓妍","刘诗诗","邓紫棋","赵丽颖","彭于晏","李亚鹏","宋茜","钟汉良","邓超","李易峰","吴昕","韩红","俞灏明","马苏","张馨予","郑恺","金秀贤","王丽坤","陈晓","郑秀文","井柏然","刘恺威","林志玲","佘诗曼","尚雯婕","赵又廷","古天乐","王俊凯","李连杰","陈妍希","孙红雷","王源","陈伟霆","吴亦凡","赵本山","ELLA陈嘉桦","华晨宇","吴镇宇","陈翔","鹿晗","尼坤","EXO-LAY","黄子韬","黄宗泽","易烊千玺","李炜","武艺","乔振宇","孙楠","姚贝娜","EXO-M","TFboys组合","李宇春","欧豪","古巨基","陶喆","李钟硕","五月天","吴世勋","杨洋","SuperJunior","EXO","周杰伦","谢霆锋"]

ALL_NAMES = ["范冰冰","张智霖","钟欣桐","张翰","陆毅","柳岩","郭采洁","五月天阿信","李晨","孙俪","周笔畅","陈建州","蔡卓妍","刘诗诗","邓紫棋","赵丽颖","彭于晏","李亚鹏","宋茜","钟汉良","邓超","李易峰","吴昕","韩红","俞灏明","马苏","张馨予","郑恺","金秀贤","王丽坤","陈晓","郑秀文","井柏然","刘恺威","林志玲","佘诗曼","尚雯婕","赵又廷","古天乐","王俊凯","李连杰","陈妍希","孙红雷","王源","陈伟霆","吴亦凡","陈嘉桦","华晨宇","吴镇宇","陈翔","鹿晗","尼坤","EXO-LAY","黄子韬","黄宗泽","易烊千玺","李炜","武艺","乔振宇","孙楠","EXO-M","TFboys组合","欧豪","古巨基","陶喆","李钟硕","五月天","吴世勋","杨洋","SuperJunior","EXO","周杰伦","谢霆锋"]
DAYS = 30

global all
all = 0

global time_over
time_over = 0

global jumptop
jumptop = 0


cookie = 'SINAGLOBAL=2880542315542.6978.1418828903535; __utma=15428400.50645057.1422260846.1422260846.1422709170.2; __utmz=15428400.1422709170.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E5%BE%AE%E5%8D%9A%E5%90%8D%E4%BA%BA%E6%A6%9C; un=jaydenhpj@gmail.com; myuid=2119643392; wvr=6; _s_tentry=sports.sina.com.cn; Apache=8339976544957.608.1423489831972; ULV=1423489832016:115:21:5:8339976544957.608.1423489831972:1423449300649; SUS=SID-2119643392-1423489835-GZ-t8n4c-7f94e6f5ac4fe7e72cbacdd9f59d29e7; SUE=es%3D23ddeac978727647bad2d1faffcf7857%26ev%3Dv1%26es2%3Dd385c1070ad9cad4f3944e82dc420623%26rs0%3DMkXPR0s8H1h3JUujk%252FgnPp%252FoXl0Bi2tMeyqUmC2OJXub0C7D9CKlBzUDOfFZkkWb3Ron5tf3%252B6CYT3eM5xTjwhZm%252FXZYovl8vqeOJIgLFOcbpNE%252BAZIXjsrhNkU2qxe26o%252BKxGOr3WRvaOSxyLRtuzZLreQn%252Bx%252FeZbijtLdYVs0%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1423489834%26et%3D1423576234%26d%3Dc909%26i%3D29e7%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D2119643392%26name%3Djaydenhpj%2540gmail.com%26nick%3D131%252A%252A%252A%252A%252A082%2540sina.cn%26fmp%3D%26lcp%3D2012-11-18%252012%253A10%253A34; SUB=_2A2553Mt6DeTxGeRP6lsX9C3Pwj6IHXVaq7uyrDV8PUNbvtBeLWX2kW93CUiPwZGuImvMfVQPEYa5CJX2UA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFUql94o83pgMYF__CGo0vv5JpX5KMt; SUHB=0d4vCHUtPU_Zj1; ALF=1455025834; SSOLoginState=1423489835; UOR=app.hustonline.net,widget.weibo.com,www.baidu.com'  # get your cookie from Chrome or Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'cookie': cookie
}

#get between string
def txt_wrap_by(start_str, end, html):
    start = html.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = html.find(end, start)
        if end >= 0:
            return html[start:end].strip()

def my_print(string):
    print string.decode('UTF-8').encode(type) 
    

def get_a_weibo_time(computer_url):
    weibo_time = 0
    req = urllib2.Request(computer_url, headers=headers)
    
    print computer_url

    while weibo_time == 0:
        try:
            time.sleep(random.randint(4, 10))
            text = urllib2.urlopen(req, None, timeout = 30).read()

            patt_view = '<script>FM.view\((.*)\)</script>'
            patt = re.compile(patt_view, re.MULTILINE)
            weibo_scripts = patt.findall(text)

            pattern = re.compile(r"date=\\\"\d+\\\"")
   
            match = pattern.findall(text)
            if len(match) > 0:
                weibo_time = re.findall(r'(\w*[0-9]+)\w*',match[-1])[0]
  
        except:
            print 'network is bad2 ,try again'
            
    #miao shu 
    return (int)(weibo_time)/1000
    
def parse_weibos_content(name, page_content, days):
    soup1 = BeautifulSoup(page_content)	#WOW...we got the soup
    
    #computer url
    
    computer_url_pre = "http://weibo.com/" + txt_wrap_by("/", "/", soup1.find_all("div",{"class":"tip2"})[0].a["href"]) + "/"
     
    all_weibo_details = soup1.find_all("div",{"class":"c"})

    soup2 = BeautifulSoup(page_content)	#WOW...we got the soup

    #bian li weibo liebiao
    #zhiding gongneng!
    #temp = del all_weibo_details[len(all_weibo_details)- 2, len(all_weibo_details)]
    all_weibo_details.pop()
    all_weibo_details.pop()
    
    i = 0
    for a_weibo_detail_pre in all_weibo_details:
        global jumptop
        global time_over
        
        i = i + 1
    
        print "id::" + a_weibo_detail_pre["id"]
        a_weibo_detail = a_weibo_detail_pre["id"].split('_')[1]
        
        computer_url = computer_url_pre + a_weibo_detail
        
        if  (get_FromtableByUrl(computer_url) != 0):
            time_over = 1
            print "3333333333333333333333"
            print get_FromtableByUrl(computer_url)
            print computer_url
            break
            
        weibo_time = get_a_weibo_time(computer_url)
        if  weibo_time == 0:
            print "4444444444444444444444"
            jumptop = jumptop + 1
            continue
        if (time.time() > (weibo_time + days * 24 * 3600)) and jumptop !=0:
            print time.time()
            print weibo_time
            print (time.time() - weibo_time)/ 24 * 3600
            time_over = 1
            print "11111111111111111111111111"
            break
        elif(time.time() > (weibo_time + days * 24 * 3600)) and jumptop ==0:
            jumptop = jumptop + 1
            print "22222222222222222222222222"
            continue
        jumptop = jumptop + 1
        print computer_url
        
        #repost
        regex = "http://weibo.cn/repost/" + a_weibo_detail
        repost_pre = soup1.find_all(href=re.compile(regex))[0].get_text()
        repost_num = re.findall(r'(\w*[0-9]+)\w*',repost_pre)[0]
        
        #comment
        regex = "http://weibo.cn/comment/" + a_weibo_detail
        comment_pre = soup1.find_all(href=re.compile(regex))[0].get_text()
        comment_num = re.findall(r'(\w*[0-9]+)\w*',comment_pre)[0]
        
        #attitude
        regex = "http://weibo.cn/attitude/" + a_weibo_detail
        attitude_pre = soup1.find_all(href=re.compile(regex))[0].get_text()
        attitude_num = re.findall(r'(\w*[0-9]+)\w*',attitude_pre)[0]
        
        insert_details2table(name, computer_url, time.ctime(weibo_time), repost_num, comment_num, attitude_num)
        
        print repost_num
        print comment_num
        print attitude_num
        
        time.sleep(random.randint(4, 8))

        # if i == len(all_weibo_details) - 3:
            # break;
    global all
    all = all + i
           

def visit(name, url, days):
    req = urllib2.Request(url, headers=headers)
    
    while True:
        try:
            time.sleep(random.randint(2, 7))
            text = urllib2.urlopen(req, None, timeout = 30).read()
            
        except:
            print 'network is bad1 ,try again'
        else:
            break
    parse_weibos_content(name, text, days)

#get user url, example http://weibo.cn/laoluoyonghao
def get_user_url(username):
    print username.decode('utf8','ignore')
    search_url = "http://s.weibo.com/user/" + username
    
    while True:
        time.sleep(random.randint(5, 10))
        try:
            req = urllib2.Request(search_url, headers=headers)
            text = urllib2.urlopen(req, None, timeout = 30).read()
        except:
            print 'network is bad3 ,try again'
        else:
            break;

    patt_view = '<script>STK && STK.pageletM && STK.pageletM.view\((.*)\)</script>'
    patt = re.compile(patt_view, re.MULTILINE)
    weibo_scripts = patt.findall(text)
    
    html = text
    for script in weibo_scripts:
        view_json = json.loads(script)
  
        if 'html' in view_json and view_json['pid'] == 'pl_user_feedList':
            html = view_json['html']
    
    soup = BeautifulSoup(html)	#WOW...we got the soup
    
    #computer url

    all_weibo_users_url = soup.find_all("div",{"class":"list_person clearfix"})    

    url = 0
    try:
        url = all_weibo_users_url[0].div.a["href"].replace("com/", "cn/")
    except:
        print "xia biao yi chang"
    return url

#get data from url ,limit in days
def get_weibo_in_days(name, url, days):

    print url

    ii = 1

    global time_over
    global all
    global jumptop
    time_over = 0
    while time_over == 0:
        print "page::" + str(ii)
        
        url_new = url + '?page=' + str(ii)
        print "page::" + url_new
        visit(name, url_new, days)
        ii = ii + 1
        print all

    print all
    time_over = 0
    all = 0
    jumptop = 0
    
def insert_details2table(User_Name, Weibo_Url, Weibo_Time, Repost_Count, Comment_Count, Attitude_Count):
    #建立和数据库系统的连接
    conn = MySQLdb.connect(host='localhost', user='root',passwd='0728abc',db='weibo',charset='utf8')

    #获取操作游标
    cursor = conn.cursor()
    
    T = (0, User_Name, Weibo_Url, Weibo_Time, Repost_Count, Comment_Count, Attitude_Count)
    
    #插入一条数据
    cursor.execute("insert into weibo_details values(%s, %s,%s,%s,%s,%s,%s)", T)
    
    cursor.close()
    conn.commit()
    conn.close()

def get_FromtableByUrl(Weibo_Url):
    #建立和数据库系统的连接
    conn = MySQLdb.connect(host='localhost', user='root',passwd='0728abc',db='weibo',charset='utf8')

    #获取操作游标
    cursor = conn.cursor()
   
    
    #插入一条数据
    m = cursor.execute("select *from weibo_details where Weibo_Url = %s", Weibo_Url)
    
    cursor.close()
    conn.commit()
    conn.close()
    
    return m
    
    
def Save_LastName(Name):
    #建立和数据库系统的连接
    conn = MySQLdb.connect(host='localhost', user='root',passwd='0728abc',db='weibo',charset='utf8')

    #获取操作游标
    cursor = conn.cursor()
    
    #插入一条数据
    m = cursor.execute("select *from memory where Id_P = 1")

    T = (0, Name)
    if m == 0:
        cursor.execute("insert into memory values(%s, %s)", T)
    else:
        cursor.execute("update memory set Last_Name = %s where Id_P = 1", Name)
        
    cursor.close()
    conn.commit()
    conn.close()

def Get_LastName():
    #建立和数据库系统的连接
    conn = MySQLdb.connect(host='localhost', user='root',passwd='0728abc',db='weibo',charset='utf8')

    #获取操作游标
    cursor = conn.cursor()
    
    #插入一条数据
    m = cursor.execute("select *from memory where Id_P = 1")
      

    
    m = cursor.fetchone()[1]
    cursor.close()
    conn.commit()
    conn.close()
    
    return m

def Delete_LastName_Details(Name):
    #建立和数据库系统的连接
    conn = MySQLdb.connect(host='localhost', user='root',passwd='0728abc',db='weibo',charset='utf8')

    #获取操作游标
    cursor = conn.cursor()
    
    #插入一条数据
    cursor.execute("delete from weibo_details where User_Name = %s", Name)
      
    cursor.close()
    conn.commit()
    conn.close()

def get_all_users_weibos(names, days):
    print 'start get data!!!'

    first = 0
    for name in names:

        if name.decode('utf8','ignore') != Get_LastName() and first == 0:
            continue
        Save_LastName(name)
        
        url = 0
        while url == 0:
            url = get_user_url(name)
        
        get_weibo_in_days(name, url, days)
        time.sleep(random.randint(20, 30))
        first = 1
        
    print 'finish get data!!!'

if __name__ == '__main__':
    Delete_LastName_Details(Get_LastName())
    get_all_users_weibos(ALL_NAMES, DAYS)
        
    x = 1
    while x == 1:
        x = 1
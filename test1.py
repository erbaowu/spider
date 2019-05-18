#判断字符串是否是整数、浮点数、复数
'''def isNum(str):
    print(isinstance(str,(int,float,complex)))'''
#判断是否是质数
'''def isPrime(i):
    l=[]
    for x in range(2,i):
        if i%x==0:
            l.append(x)
    if len(l)==0:
        print(True)
    else:
        print(False)
isPrime(24)'''
#编写函数计算传入的数字、字母、空格和其他字符的个数
'''def counts(str):
    m=n=x=y=0
    for i in str:
        if (i>='a'and i<='z') or (i>='A'and i<='Z'):
            m=m+1
        elif i>='0' and i<='9':
            n=n+1
        elif i==' ':
            x=x+1
        else:
            y=y+1
    print('字母的个数是：',m,'数字的个数是：',n,'空格的个数是：',x,'其他字符的个数是:',y,)
counts(' 1 x X ')'''

#打印200以内所有的质数
'''def printz():
     for i in range(2,201):
        l=[]
        for x in range(2,i):
            if i%x==0:
                l.append(x)
        if len(l)==0:
            print(i)
        else:
            pass
printz()'''
#斐波那契数列的第n个数
'''def fib(n):
    if n==1 or n==2:
	    return 1
    else:
	    return fib(n-1)+fib(n-2)
'''
#随机密码生成
import random
'''ls=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9]
for i in range(1,11):
    sj=random.sample(ls,8)
    print (sj)'''

#英文字符频率统计
'''s=input('请输入一个英文字符串:')
    #忽略大小写，简化问题
text=s.upper()
    #解决符号问题
for ch in '!"#$%&()*+,-./;<=>?@[\\]^_{|}~`' or ' ':
    text=text.replace(ch,'')
    #引入空字典
counts={}
words=text
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)'''
#中文字符频率统计
'''s=input('请输入一个中文字符串:')
    #忽略大小写，简化问题
    #解决符号问题
for ch in '!"#$%&()*+,-./;<=>?@[\\]^_{|}~`' or ' ':
    s=s.replace(ch,'')
    #引入空字典
counts={}
words=s
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)'''

'''ls=[
        ['指标','2014年','2015年','2016年'],
        ['居民消费价格指数','102','101.4','102'],
        ['食品','103.1','102.3','104.6'],
        ['烟酒及用品','994','102.1','101.5'],
        ['衣着','102.4','102.7','101.4'],
        ['家庭设备和用品','101.2','101','100.5'],
        ['医疗保健和个人用品','101.3','102','101.1'],
        ['交通和通信','99.9','98.3','98.7'],
        ['娱乐教育文化','101.9','101.4','101.6'],
        ['居住','102','100.7','101.6']
    ]
f=open('test1.csv','w+',encoding='utf-8')
for row in ls:
    f.write('-'.join(row))
a=f.read()
print(a)
f.close()'''
#文件中的大小写相反转化
'''f=open('eng.txt','r')
a=f.readlines()
z=open('test2.txt','a')
for lines in a:
    for alpha in lines:
        if alpha==alpha.upper():
            z.write(alpha.lower())
        else:
            z.write(alpha.upper())
f.close()
z.close() '''
#查询某字符在文件中出现的次数
'''doc=input("请输入文件内容:")
f=open('test3.txt','w',encoding='utf-8')
f.write(doc)
zf=input('请输入需要查询的字符:')
ls=[]
for item in doc:
    if item==zf:
        ls.append(item)
    else:
        pass
print(len(ls))
f.close()'''
#生成随机矩阵
'''import random
f=open('test4.txt','w')
z=open('test2.csv','w')
ls=[]
for m in range(0,10):
    for x in range(0,10):
        ls=random.randint(1,100)
        f.writelines('{:5}'.format(ls)+' ')
        z.writelines('{:5}'.format(ls)+' ')
    f.writelines('\n')
    z.writelines('\n')
f.close()
z.close()'''
#生成10个随机数列表
'''import random
ls=[]
for i in range(10):
    x=random.randint(0,101)
    ls.append(x)
print(ls)'''
#时间格式化
'''import time
a=time.localtime()
b=time.strftime("%A,%m.%B %Y %H %M %p",a)
print(b)'''
#对字符串分词并且返回列表
'''import jieba
ls=[]
s='Python是最有意思的编程语言'
x=jieba.lcut(s)
ls=x
print(ls)'''
#分词并输出结果
'''import jieba
s='今天晚上我吃了意大利面'
jieba.add_word('意大利面')
i=jieba.lcut(s)
print(i)'''
#淘宝商品比价
import re
import requests
def getHTMLText (url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def getHTMLTextFomFile(dir):
    try:
        with open(dir, encoding='utf-8') as f:
            content=f.read()
            return content
        f.close()
    except:
        return ''

def parsepage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        print(len(tlt))
        for i in range(len(plt)):
            print(i)
            print(plt[i],tlt[i])
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([title,price])
    except:
        print('')

def printgoodslist(ilt):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','商品名称'))
    count=0
    for g in ilt:
        count+=1
        print(count,g[0],g[1])

def main():
    goods='书包'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    
    infolist=[]
    dir = 'sample.html'
    html = getHTMLTextFomFile(dir)
    parsepage(infolist, html)
    printgoodslist(infolist)
    """
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsepage(infolist,html)
        except:
            continue
    printgoodslist(infolist)
    """

if __name__ == "__main__":
    main()
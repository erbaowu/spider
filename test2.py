import re
import requests
from bs4 import BeautifulSoup

def gethtmltext(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def parsrpage(ls,html):
    soup=BeautifulSoup(html,'html.parser')
    x=soup.find_all('ul',{'class':'f-hide'})
    for h in x:
        m=h.find_all('a',{'href':re.compile('song')})
        for i in m:
            print(i.text)





def main ():
    url='https://music.163.com/discover/toplist'
    html=gethtmltext(url)
    ls=[]
    parsrpage(ls,html)

if __name__ == "__main__":
    main()
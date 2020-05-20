import requests
from bs4 import BeautifulSoup,element

def getHTMLText(url):
    try:
        re = requests.get(url,timeout=30)
        re.raise_for_status()
        re.encoding=re.apparent_encoding
        return re.text
    except :
        return ''

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[4].string,])
    

def printUnivList(ulist,num):
    print("Suc"+str(num))
    print("{:-^10}{:*^60}{:#^10}".format('排名','学校名称','总分',))
    for i in range(num):
        print("{:-^10}{:*^60}{:#^10}".format(ulist[i][0],ulist[i][1],ulist[i][2],))

def __main__():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)

__main__()
import re
import requests
def getHTML(url):
   try:
     kd={'User-Agent':'Mozilla/5.0'}
     r=requests.get(url,headers=kd)
     r.raise_for_status()
     r.encoding=r.apparent_encoding
     return r.text
   except :
       return "获取网页异常"
def fenxiHTML(li,html):
    try:
       price=re.findall(r'"view_price":"[\d\.]*"',html)
       title=re.findall(r'"raw_title":".*?"',html)
       for i in range(len(price)):
          price1=eval(price[i].split(':')[1])
          title1=eval(title[i].split(':')[1])
          li.append([price1,title1])
    except:
         print("解析出错")
def printGoodlist(li):
      geshi="{:4}\t{:6}\t{:29}"
      print(geshi.format("序号","价格","名称"))
      cout=0
      for g in li:
          cout=cout+1
          print(geshi.format(cout,g[0],g[1]))
def main():
    goods=""
    goods=input("请输入你要查找的商品")
    page=2
    url1="https://s.taobao.com/search?q="+goods
    inforlist=[]
    for i in range(page):
       try:
           url2=url1+'&s='+str(44*i)
           html=getHTML(url2)
           fenxiHTML(inforlist,html)
       except:
            continue
    printGoodlist(inforlist)
main()

from datetime import datetime, date, time
import os
pathfolder=os.getcwd()
today = date.today()
monthdate="{}.{}".format(today.month, today.year)

if monthdate == "1.2018":
    cd="января"
    datm="апреля"
elif monthdate == "2.2018":
    cd="февраля"
    datm="мая"
elif monthdate == "3.2018":
    cd="марта"
    datm="июня"
elif monthdate == "4.2018":
    cd="апреля"
    datm="июля"
elif monthdate == "5.2018":
    cd="мая"
    datm="августа"
elif monthdate == "6.2018":
    cd="июня"
    datm="сентября"
elif monthdate == "7.2018":
    cd="июля"
    datm="октября"
elif monthdate == "8.2018":
    cd="авугста"
    datm="ноября"
elif monthdate == "9.2018":
    cd="сентября"
    datm="декабря"
elif monthdate == "10.2018":
    cd="октября"
    datm="января"
elif monthdate == "11.2018":
    cd="ноября"
    datm="февраля"
elif monthdate == "12.2018":
    cd="декабря"
    datm="марта"
else:
    cd="Ошибка"
    
for i in range(1,32):
    b=str(i)
    os.mkdir(pathfolder+"\\"+b+"."+monthdate)
    f=i+1
    for m in range(1,15):
        c=str(m)
        os.mkdir(pathfolder+"\\"+b+"."+monthdate+"\\"+c)
        m+=1
        f=open(pathfolder+"\\"+b+"."+monthdate+"\\"+c+"\\"+"text.html",'w', encoding="utf-8")
        f.write("<p></p><br>" + "\n" + "<h3>Вы можете выбрать из&nbsp;следующих опций:</h3><br>" + "\n" + "<ul>" + "\n" + "  <li><strong>22&nbsp;руб.</strong> за&nbsp; (<strong>вместо&nbsp;22&nbsp;руб.</strong>); </li>" + "\n" + "</ul>" + "\n" + "<br>" + "\n"+ "<ul>" + "\n" + '  <li><a href="" target="_blank"></a></li>' + "\n" + "</ul><br>" + "\n" + " " + "\n" + " " + "\n" +  "<ul><li><strong>Срок действия сертификатов:</strong> с&nbsp;20&nbsp;"+cd+" до&nbsp;20&nbsp;"+datm+"&nbsp;2018&nbsp;г.&nbsp;(включительно).</li>" + "\n"+"\n"+"</ul>" + "\n" + "\n" + "\n" + "\n" +  "..............................................................................................................................................................." + "\n" + "\n" + "<ul>" + "\n" + "\n" + "</ul>" + "\n")


    i+=1

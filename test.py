
import datetime
time =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


with open("aaa.txt","w",encoding="utf-8") as f:
    f.write(time)
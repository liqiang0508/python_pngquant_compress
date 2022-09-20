import time
data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
with open("aaa.txt", "w") as f:
    f.write(data)
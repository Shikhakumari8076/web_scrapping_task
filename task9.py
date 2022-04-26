import os
import json
import time
import random
file=open("task5.json","r+")
a=json.load(file)
file.close()

ti=random.randint(1,3)
for i in a:
    path="/home/admin123/Desktop/Web-scrapping/task9/task9"+i["movie name"]+".json"
    if os.path.exists(path):
        pass
    else:
        data=open(path,"w+")
        json.dump(i,data,indent=4)
    time.sleep(ti)
# print(ti)
            

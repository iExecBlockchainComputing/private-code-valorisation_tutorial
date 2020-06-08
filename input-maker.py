import random

s = ""
for i in range(1000):
   s = s+str(random.randint(0,10000))+","

s = s+str(random.randint(0,10000))

f = open("input_data2.csv", "w")
f.write(s)
f.close()

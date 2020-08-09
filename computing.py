import os
import re
import matplotlib.pyplot as plt

file_dir = "E:/code/RECENT-WORK/BCPNet/experiments/"
files = os.listdir(file_dir)
files = [f for f in files if f.split(".")[-1]=="txt"]

power_dicts=dict()

for f in files:
    power_dicts[f.split(".")[0]]=[]

    content = open(file_dir+f, "r")

    line_conter = 0
    for line in content:
        line_conter+=1
        if line[0]=="#":
            continue
        else:
            power=re.sub("\s+", " ", line).strip(" ").strip("-").strip().split(" ")
            assert  len(power)==3
            power = power[-2]

            if len(power_dicts[f.split(".")[0]])<500:
                power_dicts[f.split(".")[0]].append(float(power))

color=["blue", "red", "black", "lime", "magenta"]
legend =["batch=1, input_size=512x512", "batch=1, input_size=512x1024", "batch=10, input_size=512x1024", "batch=30, input_size=512x1024", "batch=50, input_size=512x1024"]

plt.plot(range(200), power_dicts["bacpnet_1_512x512"][100:300], c=color[0], label=legend[0])
plt.plot(range(200), power_dicts["bacpnet_1_512x1024"][100:300], c=color[1], label=legend[1])
plt.plot(range(200), power_dicts["bacpnet_10_512x1024"][100:300], c=color[2], label=legend[2])
plt.plot(range(200), power_dicts["bacpnet_30_512x1024"][100:300], c=color[3], label=legend[3])
plt.plot(range(200), power_dicts["bacpnet_50_512x1024"][100:300], c=color[4], label=legend[4])

plt.ylim(10, 200)
plt.xlabel("time (s)")
plt.ylabel("power (W)")
plt.legend()
plt.show()
print("*deubg*")




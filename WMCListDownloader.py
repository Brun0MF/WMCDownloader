import WMCDownloader as wmcd
import sys

searchList = []
f = open(sys.argv[2],'r')
lines = f.readlines()
for x in lines:
    searchList.append(str(x.replace('\n','')))
f.close()

print(searchList)

print("Process Started!")

count = 0
slcount = len(searchList)

for sl in searchList:
    print("("+str(count)+"/"+str(slcount)+")")
    wmcd.download_images(sl, max_images=sys.argv[1])
    count+=1

print("Process Finished!")
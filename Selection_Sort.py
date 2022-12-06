#porgram sorts the list using selection sort algorithm 
import time
import random

def selectionSort(lst):
   for i in range(0,len(lst)-1):
       minpos=i
       for j in range(i+1,len(lst)):
           if lst[j]<lst[minpos]:
               minpos = j
       lst[i],lst[minpos] = lst[minpos],lst[i]
       
'''
def selectionSort(nlist):
   for i in range(len(nlist)-1,0,-1):
       maxpos=0
       for j in range(1,i+1):
           if nlist[j]>nlist[maxpos]:
               maxpos = j
       nlist[i],nlist[maxpos] = nlist[maxpos],nlist[i]
'''
nlist=[]
for i in range(1000):
   num = random.randint(0,100)
   nlist.append(num)
   
start = time.time()
selectionSort(nlist)
end = time.time()
print(nlist)
print(end-start)

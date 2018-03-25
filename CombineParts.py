#!/usr/bin/python

import sys
import os.path
import os
import timeit
import subprocess
from math import log
from math import exp
import numpy
from math import lgamma

ID=str(sys.argv[1])
#set ID
#set error

#read in data file
#data should contain ID, I_KOBS, I_N, F_KOBS, F_N
#set nfinal


nfinal=int(13107200)
print I_KOBS, I_N
print F_KOBS, F_N

def choose(n, k):
    if k>n: out=float("-inf")
    elif k==0: out=0
    elif k==n: out=0
    else: out=lgamma(n+1)-(lgamma(k+1)+lgamma(n-k+1))
    return(out)
    
def partB1(true, obs, n, e=error):
    total=0
    last=0
    if obs==true:
        total=exp(n*log(1-e))
    else: 
        for i in range(0, obs+1):
            out=exp(choose(true, i)+(i*log(1-e))+((true-i)*log(e))+choose(n-true, obs-i)+((obs-i)*log(e))+(log(1-e)*((n-true)-(obs-i))))
            total=total+out
            if out<10**-100 and last>out:
                break
            else: last=out 
    return(total)

A=dict() 
#set partAinfile   
with open(partAinfile+ID+".txt", "r") as partA:
    next(partA)
    for line in partA:
        words=line.split()
        A[words[0]]=float(words[1])

#set PartB2B3infile
#set CombinedPartsoutfile
allvalues=0
header=["OBS", "Prob"]
with open(CombinedPartsoutfile+ID+".txt", "w") as outfile:
    outfile.write("\t".join(header))
    outfile.write("\n")
    previous=0
    for OBS in range(0, F_N+1):
        total=0
        lastA=0        
        for a in range(0, 201):
            B2B3=list()
            B=0
            with open(PartB2B3+ID+"/"+str(a)+".txt", "r") as partB2B3:
                next(partB2B3)
                for line in partB2B3:
                    words=line.split()
                    B2B3.append(float(words[1]))
            last=0
            if A[str(a)]<10**-50 and lastA>A[str(a)]:
                break
            else:
                lastA=A[str(a)]
                for true in range(0, F_N+1):
                    B1=partB1(true, obs=OBS, n=F_N)
                    B_new=B1*B2B3[true]
                    B=B+B_new
                    if B_new<10**-50 and last>B_new:
                        break
                    else: last=B_new
                out=A[str(a)]*B
                total=total+out
        allvalues=allvalues+total
        outtext=[str(OBS), str(total)]
        print outtext
        outfile.write("\t".join(outtext))
        outfile.write("\n")
        if total<10**-100 and previous>total:
            lastpos=OBS+1
            total=0.0
            break
        else:
            previous=total
    for OBS in range(lastpos, F_N+1):
        outtext=[str(OBS), str(total)]
        print outtext
        outfile.write("\t".join(outtext))
        outfile.write("\n")        
            

        
print allvalues


    

    
        
    

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

#set a value, ID
#read in data
#data should contain ID, I_KOBS, I_N, F_KOBS, F_N
#set nfinal

#read in Moran model data from infile (DriftforErrorModel.py)
B3=list()
if os.path.exists(infile+"ni=200/nf=13107200/ki="+str(a)+".txt"):
    with open(infile+"ni=200/nf=13107200/ki="+str(a)+".txt", "r") as infile:
        for line in infile:
            words=line.split()
            B3.append(float(words[0]))
else: print "No File!"
print "Done Reading"

def choose(n, k):
    if k>n: out=float("-inf")
    else: out=lgamma(n+1)-(lgamma(k+1)+lgamma(n-k+1))
    return(out)
    

def B2B3(a, true, n=F_N):
    total=0
    last=0
    for kfinal in range(0, nfinal):
        if kfinal==0:
            if true==0: B2=0.0
            else: B2=float("-inf")
        elif kfinal==nfinal:
            if true==n: B2=0.0
            else: B2=float("-inf")
        else: B2=choose(n, true)+(true*log(float(kfinal)/float(nfinal)))+((n-true)*log(1-float(kfinal)/float(nfinal)))
        total=total+exp(B2)*B3[kfinal]
#        print kfinal, total, exp(B2), B3[kfinal]
        if exp(B2)<10**-100 and last>exp(B2):
            break
        else: last=exp(B2)        
    print true, total
    return(total)

   
#set outfilename
header=["True", "Prob"]
if not os.path.exists(outfilename+ID+"/"):
    os.makedirs(outfilename+ID+"/")              
total=0
with open(outfilename+ID+"/"+str(a)+".txt", "w") as outfile:
    outfile.write("\t".join(header))
    outfile.write("\n")
    for true in range(0, F_N+1):
        B=B2B3(a, true)
        outfile.write("\t".join([str(true),str(B)]))
        outfile.write("\n")
        total=total+B

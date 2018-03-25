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


ses=[0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, -0.01, -0.05, -0.1, -0.15, -0.2, -0.25, -0.3, -0.4, -0.5, -0.6, -0.7, -0.8, -0.9]
print ID

#set error
#read in data
#data should contain ID, I_KOBS, I_N, F_KOBS, F_N
#set nfinal

print I_KOBS, I_N
print F_KOBS, F_N

def choose(n, k):
    if k>n: out=float("-inf")
    else: out=lgamma(n+1)-(lgamma(k+1)+lgamma(n-k+1))
    return(out)
    

def B2B3(true, n=F_N):
    total=0.0
    last=0
    for kfinal in B3.keys():
        if kfinal=="0":
            if true==0: B2=0.0
            else: B2=float("-inf")
        elif kfinal==nfinal:
            if true==n: B2=0.0
            else: B2=float("-inf")
        else: B2=choose(n, true)+(true*log(float(kfinal)/float(nfinal)))+((n-true)*log(1-float(kfinal)/float(nfinal)))
        
        total=total+exp(B2)*B3[kfinal]   
    return(total)

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
    
#set joint dsitributions infile
like=dict()
for s in ses:
    B3=dict()
    if os.path.exists(jointdistributionsinfile+ID+"/s="+str(s)+"/Combined_exact.txt"):
        with open(jointdistributionsinfile+ID+"/s="+str(s)+"/Combined_exact.txt", "r") as infile:
            total=0
            next(infile)
            for line in infile:
                words=line.split()
                kf=int(words[0])
                count=int(words[1])
                B3[str(kf)]=count
                total=total+count
    else: print "No Selection Matrix File!"
#    print "Done Reading"

    B3.update((x, y/float(total)) for (x, y) in B3.items())



    B=dict()
    for true in range(0, F_N+1):
        B[str(true)]=B2B3(true)
    

    like[str(s)]=0
    for true in range(0, F_N+1):
        like[str(s)]=like[str(s)]+partB1(true, obs=F_KOBS, n=F_N)*B[str(true)]
    
    
#set likelihoodoutfile
header=["s", "Prob"]          
with open(likelihoodoutfile+ID+".txt", "w") as outfile:
    outfile.write("\t".join(header))
    outfile.write("\n")
    for s in ses:
        outfile.write(str(s)+"\t"+str(like[str(s)])+"\n")

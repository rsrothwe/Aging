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
            
#set error
#read in data
#data should contain ID, I_KOBS, I_N, F_KOBS, F_N
#set nfinal


def choose(n, k):
    if k>n: out=float("-inf")
    elif k==0: out=0
    elif k==n: out=0
    else: out=lgamma(n+1)-(lgamma(k+1)+lgamma(n-k+1))
    return(out)


def seqerror(true, obs, n, e=error):
    total=0
    last=0
    if obs==true:
        total=exp(n*log(1-e))
    else: 
        for i in range(0, true+1):
            out=exp(choose(obs, i)+(i*log(1-e))+((obs-i)*log(e))+choose(n-obs, true-i)+((true-i)*log(e))+(log(1-e)*((n-obs)-(true-i))))
            total=total+out
            if out<10**-100 and last>out:
                break
            else: last=out
    return(total)
        
        
def partA(a, true, obs=I_KOBS, n=I_N):
    A1=seqerror(true, obs, n)
    A2=choose(200,a)
    A3=lgamma(a+true+1)+lgamma((200-a)+(n-true)+1)+lgamma(n+2)
    A4=lgamma(200+n+2)+lgamma(true+1)+lgamma(n-true+1)
    out=A1*exp(A2+A3-A4)
    return(out)


#set outfilename
total=0
header=["a", "Prob"]              
with open(outfilename+".txt", "w") as outfile:
    outfile.write("\t".join(header))
    outfile.write("\n")
    for a in range(0, 201):
        A=sum([partA(a, true) for true in range(0, I_N+1)])
        outfile.write("\t".join([str(a),str(A)]))
        outfile.write("\n")
        print a, A
        total=total+A

        
print total

       


    
    

    
        
    

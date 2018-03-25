#!/usr/bin/python

 
import sys
import numpy as np
import time
import os
import os.path
import math
import random


def round_down(x, a):
    return math.floor(x / a) * a

#set nfinal

s=float(sys.argv[1])
ID=str(sys.argv[2])
iteration=str(sys.argv[3])

ks=np.arange(0, 1.01, 0.01)
ks = [ '%.2f' % x for x in ks ]
returns=[0]*len(ks)

out=dict(zip(ks, returns))

exacts=dict()

#set partAinfilename
As=dict()
probs=list()
with open(partAinfile+ID+".txt", "r") as PartA:
    next(PartA)
    for line in PartA:
        words=(line.strip()).split("\t")
        probs.append(float(words[1]))
        As[words[0]]=words[1]
        
print "Done Reading Part A"



g=sum(probs)
normprobs=[a/g for a in (probs)]


t0=time.clock()
for i in range(0, jobs):
    a=np.ndarray.tolist(np.random.multinomial(1, normprobs)).index(1)
    k0=a
    n0=200
    while n0<nfinal:
        add=np.random.binomial(1, (k0+k0*s)/(n0+k0*s))
        k0=k0+add
        n0=n0+1
    if k0 in exacts:
        exacts[k0] += 1
    else:
        exacts[k0] = 1
    kf='%.2f' % (float(k0)/float(n0))
    print a, k0, kf, i, "\n"
    out[kf]=out[kf]+1
      
t1=time.clock()

total=t1-t0
print total

#set outfilename
with open(outfilename+ID+"/s="+str(s)+"/Iteration="+str(iteration)+"_exact.txt", "w") as outfile:
    outfile.write("kf\tProb\n")
    for k in sorted(exacts):
        outfile.write(str(k)+"\t"+str(exacts[k])+"\n")

with open(outfilename+ID+"/s="+str(s)+"/Iteration="+str(iteration)+".txt", "w") as outfile2:
    outfile2.write("Pf\tProb\n")
    for k in sorted(out):
        outfile2.write(str(k)+"\t"+str(out[k])+"\n")


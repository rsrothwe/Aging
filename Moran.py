#!/usr/bin/python

import sys
import os.path
import os
import itertools
import stat
import subprocess
from datetime import datetime
from scipy.misc import comb
from math import log
from math import exp
import numpy
from math import lgamma
import os.path

startTime = datetime.now()

ni=int(sys.argv[1])
nf=int(sys.argv[2])
kf=int(sys.argv[3])
initialdraw=200

# Creates a list containing ni lists initialized to 0

def choose(n, k):
    return(lgamma(n+1)-(lgamma(k+1)+lgamma(n-k+1)))


def moran(kf2, ni2, ki2, nf2):
    if kf2==nf2 and ki2==ni2: out=log(1)
    elif kf2==0 and ki2==0: out=log(1)
    elif (kf2!=0 and ki2==0) or (kf2!=nf2 and ki2==ni2): out=-float("inf")
    else: 
        if (nf2-ni2)<(kf2-ki2) or ki2>kf2: out=-float("inf")
        else:
            partone=choose(nf2-ni2, kf2-ki2)
            parttwo=lgamma(ki2+(kf2-ki2)-1+1)-lgamma(ki2-1+1)
            partthree=lgamma(ni2-ki2+((nf2-ni2)-(kf2-ki2)-1)+1)-lgamma(ni2-ki2-1+1)
            partfour=lgamma(ni2-1+1)-lgamma(ni2+(nf2-ni2-1)+1)
            out=partone+parttwo+partthree+partfour
    return(exp(out))
    
print "Started CondenseDriftOneFile.py"
print "ni"+str(ni)
print "nf"+str(nf)
print "kf"+str(kf)

#set driftoutfile


with open(driftoutfile+str(ni)+"/nf="+str(nf)+"/kf="+str(kf)+".txt", "w") as outfile:
    for ki in range(0, ni+1):
        if ki>kf: prob=0
        else: prob=str(moran(kf,ni,ki, nf))
        print ki
        print str(prob)
        outfile.write(str(prob))
        outfile.write("\n")

print datetime.now() - startTime

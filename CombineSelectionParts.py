#!/usr/bin/python

 
import sys

#set ID values(IDs)
#set s values

#set infilename
exacts=dict()
mafs=dict()
for i in range(0, len(s)):
    for ID in IDs:
        print ID, s[i]
        exacts=dict()
        mafs=dict()
        total=0
        for iteration in range(1, 101):
            with open(infilename+ID+"/s="+str(s[i])+"/Iteration="+str(iteration)+"_exact.txt", "r") as infile:
                next(infile)
                for line in infile:
                    words=line.split("\t")
                    k0=words[0]
                    maf=("%.2f" % (float(words[0])/13107200.0))
                        
                    if maf in mafs:
                        mafs[maf] += int(words[1])
                    else:
                        mafs[maf] = int(words[1])
                            
                    if k0 in exacts:
                        exacts[k0] += int(words[1])
                    else:
                        exacts[k0] = int(words[1])
                    total=total+int(words[1])
          
        with open(infilename+ID+"/s="+str(s[i])+"/Combined_exact.txt", "w") as outfile:
            outfile.write("kf\tCount\n")
            for k in sorted(exacts):
                outfile.write(str(k)+"\t"+str(exacts[k])+"\n")
                    
        with open(infilename+ID+"/s="+str(s[i])+"/Combined.txt", "w") as outfile:
            outfile.write("MAF\tCount\n")
            for k in sorted(mafs):
                outfile.write(str(k)+"\t"+str(mafs[k])+"\n")


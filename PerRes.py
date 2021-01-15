"""This code will take five input files: a pdb, and one solv.out file from APBSmem to calculate per residue contributions of gating charge energy, this script is redundant and probably a worse version
of what Frank has developed.This script only looks at one monomer."""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from collections import OrderedDict

def readfiles():
    """generate file pointers for pdb and solv.out files, returns five file pointers"""
    """try:
        os.chdir('C:\\Users\\mailk\\py4e')
    except:
        pass"""
    #fplist = ['fpsolv','fpsolv1','fpsolv2','fpsolv3']
    while True:
        pdbinput=input('Please enter the name of the pdb (include .pdb)')
        solvinput=input('Please enter the name of the solv.out (include .solv.out)')
        try:
            fppdb = open(pdbinput,"r")#input("pdb id + .pdb")
            fpsolv = open(solvinput,"r")
            break
            #fpsolv1 = open('10920_vSGLT_monomer_gatecharge_06.solv.out1',"r")
            #fpsolv2 = open('10920_vSGLT_monomer_gatecharge_06.solv.out2',"r")
            #fpsolv3 = open('10920_vSGLT_monomer_gatecharge_06.solv.out3',"r")
        except:
            print('Please Enter a Valid Filename')
    #fpsolvname = input('Solv file name (exclude the 'solv.out')')
    #for i in range(4):
        #fpsolv + str(i) = open(fpsolvname+str(i)
    return fppdb,fpsolv #,fpsolv1,fpsolv2,fpsolv3
def fetchatom(a,calc,line,solvdict):
    """gut checking by summing up the energies"""
    if line[6:10] == 'Atom':
        solvdict['solv'+str(a)+'sum'+str(calc)] += float(line.split()[2])
    return solvdict
def peratomsolv(peratomsolvdict,line):
    """fetches energy values from solv.out and converts to joules"""
    if line[6:10] == 'Atom':
        #can convert jouls to kT by dividing by 2.479
        peratomsolvdict[line.split()[1][:-1]] = (float(line.split()[2]))/1.2395
    return peratomsolvdict
def parsesolv(fpsolv):
    """parses all the solve files to produce a contribution of charge from each atom, returns a single dictionary that lists per atom gating charge contribution"""
    solvdict = {}
    b = 0
    c = -1
    d = -1
    e = -1
    for i in range(4):
        for j in range(6):
            solvdict[('solv'+str(i)+'sum'+str(j))] = 0
    peratomsolvdict1 = {}
    peratomsolvdict2 = {}
    peratomsolvdict3 = {}
    peratomsolvdict4 = {}
    peratomsolvdict5 = {}
    peratomsolvdict6 = {}
    #print(solvdict)
    for line in fpsolv:
        if line[:11] == 'CALCULATION':
            b+=1
        #solvdict = fetchatom(0,b,line,solvdict)
        if b == 1:
            peratomsolvdict1 = peratomsolv(peratomsolvdict1,line)
        if b == 2:
            peratomsolvdict2 = peratomsolv(peratomsolvdict2,line)
        if b == 3:
            peratomsolvdict3 = peratomsolv(peratomsolvdict3,line)
        if b == 4:
            peratomsolvdict4 = peratomsolv(peratomsolvdict4,line)
        if b == 5:
            peratomsolvdict5 = peratomsolv(peratomsolvdict5,line)
        if b == 6:
            peratomsolvdict6 = peratomsolv(peratomsolvdict6,line)
    """ gut check to compare numbers to .log file
    for line in fpsolv1:
        if line[:11] == 'CALCULATION':
            c+=1
        solvdict = fetchatom(1,c,line,solvdict)
    for line in fpsolv2:
        if line[:11] == 'CALCULATION':
            d+=1
        solvdict = fetchatom(2,d,line,solvdict)
    for line in fpsolv3:
        if line[:11] == 'CALCULATION':
            e+=1
        solvdict = fetchatom(3,e,line,solvdict)"""
    per_atom={}
    """I learned here that the third calculation is subtracted BY the 6th calculation in order to get the change in energy:
    summed=0
    summed2=0
    for hit in peratomsolvdict1.values():
        summed+=hit
    for hit in peratomsolvdict2.values():
        summed2+=hit
    print(summed-summed2)"""
    if b == 6:
        for i in range(1,len(peratomsolvdict1)):
            try:
                per_atom[str(i)] = (peratomsolvdict3[str(i)] - peratomsolvdict6[str(i)]) / 2
            except:
                pass
    elif b == 4:
        for i in range(1,len(peratomsolvdict1)):
            try:
                per_atom[str(i)] = (peratomsolvdict2[str(i)] - peratomsolvdict4[str(i)]) / 2
            except:
                pass
    elif b == 2:
        for i in range(1,len(peratomsolvdict1)):
            try:
                per_atom[str(i)] = (peratomsolvdict1[str(i)] - peratomsolvdict2[str(i)]) / 2
            except:
                pass
    return per_atom
def addpdb(per_atom,fppdb):
    """sums up residual charge for each residue, returns a dictionary that lists per residue gating charge contribution"""
    a = None
    b = 0
    c = None
    per_res = {}
    per_res_num = {}
    for line in fppdb:
        if line[:4] == 'ATOM':
            try:
                atomnum = per_atom[str(line.split()[1])]
            except:
                pass
            res3name = line[17:20] #this is residue name in 3 letter code
            aa = line[23:26] #aa is residue number
            cc = line[21:22] #cc is chain id, in case its a n-mer protein
            if line[21:22] != " ":
                try:
                    if a == None:
                        c = cc
                        a = aa
                        per_res[c + line[17:20] + str(a)] = atomnum
                    elif c != cc:
                        break
                        per_res[c + line[17:20] + str(a)] = atomnum
                    elif a == aa:
                        per_res[c + line[17:20] + str(a)] += atomnum
                    elif a != line[23:26]:
                        a = line[23:26]
                        per_res[c + line[17:20] + str(a)] = atomnum
                except:
                    pass
            elif line[21:22] == " ":
                try:
                    if a == None:
                        a = line[23:26]
                        per_res[line[17:20] + str(a)] = atomnum
                    elif a == line[23:26]:
                        per_res[line[17:20] + str(a)] += atomnum
                    elif a != line[23:26]:
                        a = line[23:26]
                        per_res[line[17:20] + str(a)] = atomnum
                except:
                    pass
    xlim=len(per_res)
    #print(per_res)
    for value in per_res.values():
        b += 1
        per_res_num[int(b)] = float(value)
    return per_res,per_res_num,xlim
def graph(per_res,per_res_num,xlim):
    """produce a graph of gating charge contribution per residue starting from residue 1"""
    per_res_num = OrderedDict(per_res_num)
    x = per_res_num.keys()
    y = per_res_num.values()
    plt.title('Per Residue Gating Charge Contributions')
    plt.xlabel('Residue#')
    plt.ylabel('Charge Contribution(e)')
    plt.plot(x, y)
    plt.ylim(-1,1)
    x_ticks = np.arange(0,xlim,50)
    plt.xticks(x_ticks)
    plt.show()
    return None
def shownotableresidues(per_res):
    sum=0
    for res in per_res.values():
        sum += res
    print('Total Gating Charge: ' + str(sum) + 'e')
    for key in per_res:
        if abs(per_res[key]) >= 0.1:
            print('Notable Residues Above 20% Total Gating Charge: ' + str(key) + ": " + str(per_res[key]))
    while True:
        try:
            resinput = input('Enter Residue Name and Number: ')
            if resinput == "quit":
                break
            else:
                print(resinput + ":" + str(per_res[resinput]))
        except:
            print("Invalid Residue Name (Use Three Letter code)")
def main():
    fppdb,fpsolv = readfiles()
    per_atom = parsesolv(fpsolv)
    per_res,per_res_num,xlim = addpdb(per_atom,fppdb)
    graph(per_res,per_res_num,xlim)
    shownotableresidues(per_res)
main()

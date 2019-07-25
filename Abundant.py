# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:43:18 2019

@author: swsim
"""
abundant =[]
ab_combinaitons=[]

def main():
    create_ablist()
    print("abundant list contains : " + str(len(abundant)))
    ab_adition()
    print("finished")
    
def ab_adition():
    p=0
    for a in abundant:
        p+=1
        print(p)
        for b in abundant:
            if (a+b)>28123:
                continue
            if (a+b) not in ab_combinaitons:
                ab_combinaitons.append(a+b)
                
                
    
def create_ablist():
    for i in range(12,28123):
        if isabundant(i):
            abundant.append(i)
    
def isabundant(x):
    y=int(x/2)+1
    tot=0
    for i in range(1,y+1):
        if(x%i==0):
            tot+=i
    if tot>x:
        return True
    else:
        return False

main()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:32:06 2020

@author: ahmed
"""
from numpy import random
class population:
    def __init__(self,ind,fit,mutate,cross):
        self.individuals=ind
        self.fit=fit# return tuple (fit,value)
        self.mutate=mutate
        self.cross=cross
    
    def mutate(self,i):
        self.individuals[i]=self.mutate(self)
    
    ## TODO:implement other techniques of selection
    def select(self):
        size=len(self.individuals)
        sumFit=sum(self.individuals)
        dist=[(self.f(i)[1]/sumFit) for i in self.individuals]
        
        parents=[]
        
        for c in range(size):
            i,j=0,0
            #chose parents
                i=random.choice(size,p=dist)
            while True
                j=random.choice(size,p=dist)
                if i!=j:## if parents are not same 
                    break
            
            parents.append((i,j))
        
        return parents
    
    def getNewPop(self,parents):
        newPop=[]
        for i,j in parents:
            offspring=self.cross(self.individuals[i],self.individuals[j])
            # mutate by random 
            if random.rand(0, 1) ## 1 indicate apply mutation
                offspring=self.mutate(offspring)
            newPop.append(offspring)
        return population(newPop,self.fit,self.mutate,self.cross)
            
        
    
                    
        
        
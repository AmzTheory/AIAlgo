# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:46:26 2020

@author: Ahmed
"""
from Frontier import *
from Problems import *

def graphSearch(problem,frontier):
    explored=dict()
    frontier.push(problem.initialState())
    while (not frontier.empty()): ## loop until queus is empty
        current=frontier.pop()
        if problem.goalTest(current.state):
            return current
        explored[current]=True
        for child in problem.actions(current):
            if not(child in explored): ## child has snot been explored yet
                frontier.push(child)
    return None

## use if no cycles
def treeSearch(problem,frontier):
    frontier.push(problem.initialState())
    while (not frontier.empty()): ## loop until queus is empty
        current=frontier.pop()
        if problem.goalTest(current.state):
            return current
        explored[current]=True
        for child in problem.actions(current):
                frontier.push(child)
    return None      




def bfs(problem):
    return graphSearch(problem,Queue())

def dfs(problem):
    return graphSearch(problem,Stack())

def dfsRec(problem,root,limit,explored):
    explored[root]=True
    ##terminating cases
    if problem.goalTest(root.state):
        return root,True   ##passed test
    if limit==0:
        return 1,False  ## indicate cut-off
    else:
        cutoff=False
        for child in problem.actions(root):
            if child in explored:##skip if explored
                continue
                
            result,found=dfsRec(problem,child,limit-1,explored)
            if found:
                return result,True
            elif result:
                cutoff=True
         
        ##traversed all nodes in the level
        if cutoff:
            return 1,False ## cutoff value
        else:
            return 0,False ## failure value

def dfsLimit(problem,limit):
    return dfsRec(problem,problem.initialState(),limit,dict())
    
def iterativeDeepining(problem):
    result,found=0,0
    limit=0
    while True:
        result,found=dfsLimit(problem,limit)
        if found:
            return result,limit
        elif not result: ##failure 
            return "failed"
            
        limit+=1##increment the limit
        
 
       
def uniformSearch(problem:InformedSearchProblem):
    return graphSearch(problem,PriorityQueue(f=lambda n:n.cost))

def greedyFirstSearch(problem:InformedSearchProblem):
    return graphSearch(problem,PriorityQueue(f=lambda n:problem.h(n)))

def aStar(problem:InformedSearchProblem):
    return graphSearch(problem,PriorityQueue(f=lambda n:n.total+problem.h(n)))
    
 
    
        
           
        

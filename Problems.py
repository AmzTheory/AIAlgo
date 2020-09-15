# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:34:49 2020

@author: Ahmed
"""
from Frontier import *
class SearchProblem():
    "An interface for problems that need to be searched"
    
    
    def initialState(self):
        pass
    
    ##actions with Cost??
    def actions(self,state):
        pass
    
    def goalTest(self,state)->bool:
        pass
    def logSolution(self,step):
        pass
        

class InformedSearchProblem(SearchProblem):
    
    def cost(self,n,m):
        pass
    
    "An interface for problem used for informed search algorithms"
    def h(sel,node):## cost to goal, using heuristic 
        pass
    

class BinaryMazeProblem(SearchProblem):
    def __init__(self,maze,cols,rows,loc,goal):
        self.maze=maze
        self.loc=loc
        self.cols=cols ##x/cols
        self.rows=rows ##y/rows
        self.goal=goal
        self.solution=[]
        
     ## 1-> allowed
     ## 2-> not allowe to use as part of path
        
        
    def initialState(self):
        return Node(self.loc)
    
    def actions(self,node):
        (x,y)=node.state
        children=[]
        
        ##left
        if x>-1:
            if(self.maze[y][x-1]):
                children.append(Node((x-1,y),node,"L",1,node.total+1))
            
        ##right
        if x<self.cols-1:
            if(self.maze[y][x+1]):
                children.append(Node((x+1,y),node,"R",1,node.total+1))
        
        
        ##top
        if y>-1:
            if(self.maze[y-1][x]):
                children.append(Node((x,y-1),node,"T",1,node.total+1))
        
        ##bottom
        if y<self.rows-1:
            if(self.maze[y+1][x]):
                children.append(Node((x,y+1),node,"B",1,node.total+1))
            
        return children
    
    
    def goalTest(self,state)->bool:
            x,y=state
            gx,gy=self.goal
            
            return x==gx and y==gy
        
    def logSolution(self,step):
        self.solution.append(step)
        
class EightPuzzle(InformedSearchProblem):
    "Defines the 8-puzzle problem"
    def __init__(self,shape,init,goal):
        self.init=init
        self.rows,self.cols=shape
        self.goal=goal
    
    def findBlank(state):
        for r in range(len(state)):
            for c in range(len(state[r])):
                if state[r][c]==-1:
                    return r,c
    
    def actions(self,node):
        cr,cc=findBlank(node.state)
    
        if cc!=0:
            pass
            
class NavigationProblem(InformedSearchProblem): 
    
    def __init__(self,graph,hn,init,goal):
        self.graph=graph
        self.init=init
        self.hn=hn
        self.goal=goal          
    
    def initialState(self):
        return Node(self.init,action=self.init)
    
    def actions(self,node):
        return [Node(e,node,e,w,node.total+w) for (e,w) in self.graph.get(node.state)]
    
    def goalTest(self,state):
        return state==self.goal
    
    def h(self,node):
        return self.hn[node.state]
            
        
    

        
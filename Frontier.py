class Node:
    "Node represent an element in the tree"
    def __init__(self,state,parent=None,action="inital",cost=0,total=0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.total=total
        self.action=action
    
    def getSolution(self):
        solution=[]
        node=self
        while(True):
            solution.append(node.action)
            if(node.parent==None):
                break
            node=node.parent
            
        solution.reverse()
        return solution  
        
class Queue:
    'Basic Implementation of queue Datastructure'
    
    def __init__(self):
        self.queue=[]
        
    ## time: constant    
    def push(self,e):
        self.queue.append(e)
        
    ## time: constant (in practice)
    def pop(self):
        return self.queue.pop(0)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[len(self.queue)-1]
    
    def empty(self):
        return len(self.queue)==0
    
    def state(self):
        return self.queue
    
    
class Stack:
    'Basic Implementation of stack Datastructure'
    
    def __init__(self):
        self.stack=[]
        
    ## time: constant    
    def push(self,e):
        self.stack.append(e)
        
    ## time: constant (in practice)
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    def empty(self):
        return len(self.stack)==0

class PriorityQueue():
    def __init__(self,typePQ="MIN",f=lambda a:a,ls=[]):
        self.heap=[]##should be a pure array
        self.compare=lambda a,b:f(a)<=f(b)
        if typePQ=="MAX": 
            self.compare=lambda a,b:f(a)>=f(b)
        self.size=0
        # if ls contain element push them
        for e in ls:
            self.push(e)
    
    def swap(self,i,j):
        temp=self.heap[i]
        self.heap[i]=self.heap[j]
        self.heap[j]=temp
        
    
    def heapifyDown(self,i):
        best=i
        leftChild=2*i
        rightChild=leftChild+1
        
        #compare left
        if leftChild<self.size and self.compare(self.heap[leftChild],self.heap[best]):
            best=leftChild
            
        #compare right
        if rightChild<self.size and self.compare(self.heap[rightChild],self.heap[best]):
            best=rightChild
        
        
        # if best is i the break
        if i==best:##no violation
            return
        
        #else swap and go furth down
        self.swap(i,best)
        self.heapifyDown(best)
        
        
    def heapifyUp(self,i):
        while i!=0:
            parent=self.heap[int(i/2)]
            child=self.heap[i]
            if self.compare(parent,child): 
                break ## break if no violation
            
            ##swap with parent
            self.swap(i,int(i/2))
            i=int(i/2)
             
    def pop(self):
        head=self.heap[0]
        self.heap[0]=self.heap[self.size-1]
        self.size-=1
        self.heapifyDown(0)
        return head
        
    ##elemen tuple of two (key,obj)    
    def push(self,elem):
        self.heap.append(elem)
        self.size+=1
        self.heapifyUp(self.size-1)
    def pushAll(self,elems):
        for e in elems:
            self.push(e)
            
        
    def empty(self):
        return self.size==0
    def peek(self):
        if self.empty():
            return self.heap[0][1]
        
        return None
            
class Graph():
    "Non directed Graph"
    
    def __init__(self,vertices):
        self.vertices=vertices ## dict of dicts
    
    def get(self,node):
        if self.vertices.get(node)==None:
            return []
        else:
            return self.vertices.get(node).items()

    def __conncect(self,node1,node2,w):
        self.vertices[node1][node2]=w
        self.vertices[node2][node1]=w
    
    
    
    
    
    
    
    
    
    
    
    
    
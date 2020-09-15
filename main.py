# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:47:33 2020

@author: Ahmed
"""

import Search,Frontier,Problems
#maze= [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
#      [1, 0, 1, 0, 1, 1, 1, 1, 1, 1 ],
#      [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
#      [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
#      [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
#      [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
#      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
#      [1, 0, 1, 0, 1, 1, 0, 1, 1, 1 ],
#      [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
#rows,cols=len(maze),len(maze[0])
#goal=(4,0) #(x,y)
#prob=BinaryMazeProblem(maze,cols,rows,(0,0),goal)
#sol=bfs(prob)

romania_map = Graph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75,craiova=183),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99,Bucharest=211),
    Hirsova=dict(Urziceni=98,Eforie=86),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=183),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142,Bucharest=85,Hirsova=98),
    Zerind=dict(Oradea=71,Arad=75),
    Timisoara=dict(Lugoj=111,Arad=118),
    Medhadia=dict(Lugoj=70,Dorbeta=75),
    Sibiu=dict(Fagaras=99,Rimnicu=80),
    Giurgiu=dict(Bucharest=90),
    Vaslui=dict(Urziceni=142,Iasi=92),
    Neamt=dict(Isai=87)))
h={"Arad":366,
   "Bucharest":0,
   "Craiova":160,
   "Drobeta":242,"Eforie":161,"Fagaras":176,
  "Giurgiu":77,"Hirsova":151,"Iasi":226,"Lugoj":244,
  "Mehadia":241,"Neamt":234,"Oradea":380,"Pitesti":100,
  "Rimnicu":193,"Sibiu":253,"Timisoara":329,"Urziceni":80,
  "Vaslui":199,"Zerind":374}


prob=NavigationProblem(romania_map,h,"Arad","Bucharest")
sol=uniformSearch(prob)
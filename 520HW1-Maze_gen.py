#!/usr/bin/env python
# coding: utf-8

# In[53]:


import math
import numpy as np
import random
from random import choices
from colorama import init, Fore


# In[59]:


class cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.b = False
        self.g = 0
        self.f = 0
        self.h = 0
        self.h_new = 0
    def set_hval(self,t_x,t_y):
        self.h = abs(t_x - self.x) + abs(t_y - self.y)
        self.f = self.g + self.h


# In[3]:


c = cell(1,2)
c.set_hval(8,9)
print(c.h, c.f)


# In[57]:


class maze:
    def __init__(self,rows,columns,sx,sy,tx,ty):
        self.rows = rows
        self.columns = columns
        self.sx = sx
        self.sy = sy
        self.tx = tx
        self.ty = ty
        self.visited = [[False for i in range(self.rows)] for j in range(self.columns)]
        self.options = ['b','u']
        self.weights = [0.3,0.7]
        self.drow = [0, 1, 0, -1]
        self.dcol = [-1, 0, 1, 0]
        #p = choices(self.options,self.weights)
        #print(p)
        self.mz = [] 
        for i in range(self.rows):
            arr = []
            for j in range(self.columns):
                c = cell(i,j)
                arr.append(c)
            self.mz.append(arr)            
    def isValid(self,r,c):
        if (r < 0 or c < 0 or r >= self.rows or c >= self.columns):
            return False
        if (self.visited[r][c]):
            return False
        return True
    def DFS(self,grid,sx,sy,tx,ty):
        stk = []
        stk.append([sx, sy])
        while(len(stk)>0):
            curr = stk[len(stk) - 1]
            stk.remove(stk[len(stk) - 1])
            r = curr[0]
            c = curr[1]
            if(self.isValid(r, c) == False):
                continue
            p = choices(self.options,self.weights)
            self.visited[r][c] = True
            if((r!= sx and c != sy) and (r!=tx or c != ty)):
                if(p[0]== 'b'):
                    self.mz[r][c].b = True
            for i in range(4):
                adjx = r + self.drow[i]
                adjy = c + self.dcol[i]
                stk.append([adjx, adjy])


# In[58]:


m = maze(10,10,0,0,9,9)
m.DFS([],0,0,9,9)
l = []
for i in range(10):
    a = []
    for j in range(10):
        if m.mz[i][j].b:
            a.append('x')
            print(Fore.RED, f'x', end="")
        else:
            a.append('-')
            print(Fore.GREEN, f'-', end="")
    l.append(a)
    print('\n')


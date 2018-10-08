# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 10:12:06 2018

@author: Shashank
"""

class MazeEnv1(object):
    
    label_to_action = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    action_to_label = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    
    
    def __init__(self,blocks):
        self.blocks = blocks
        self.build()
        self.reset()
        self.assignBlocks()
#        self.render()
        self.good=20
        self.bad=0
        self.ok=0
        self.done=False
        self.prevS=0
        
      
    def build(self):
        self.grid=[ ['_']*5 for _ in range(5) ]
    
    def playerGoesTo(self):
        prevP=self.stateToPosition(self.prevS)
        self.grid[prevP[0]][prevP[1]]='_'

        self.grid[self.playerP[0]][self.playerP[1]]='0'
        
    def reset(self):
        self.playerP = [0,0] 
        self.playerS = self.positionToState(self.playerP)
        self.prevS=0
        self.playerGoesTo()
        self.grid[4][4]='_'
        self.done = False

        
     
    def render(self):
        for i in self.grid:
            print(i)
   
      
    def stateToPosition(self,S):
        return [S//5,S%5]
    
    def positionToState(self,P):
        return P[0]*5 + P[1]

    def assignBlocks(self):
        for b in self.blocks:
            b_x,b_y = self.stateToPosition(b)
            self.grid[b_x][b_y] = '#'
    
    def takeAction(self,action):
        if(self.label_to_action[action]==0):
            hyp=self.playerS-5
        if(self.label_to_action[action]==1):
            hyp=self.playerS+5
        if(self.label_to_action[action]==2):
            hyp=self.playerS-1
        if(self.label_to_action[action]==3):
            hyp=self.playerS+1
        return hyp
    
    def isBlocked(self,action):
        hyp=self.takeAction(action)
        if(self.label_to_action[action]==0):
            if(hyp<0 or hyp in self.blocks):
               return True
            else:
                return False
           
        if(self.label_to_action[action]==1):
            if(hyp>24 or hyp in self.blocks):
                return True
            else:
                return False
        
        if(self.label_to_action[action]==2):
            if(hyp in [-1,4,9,14,19] or hyp in self.blocks):
                return True
            else:
                return False
        
        if(self.label_to_action[action]==3):
            if(hyp in [5,10,15,20,25] or hyp in self.blocks):
                return True
            else:
                return False
            
    def step(self,action_num):
        action = self.action_to_label[action_num]
        reward=0
        if(self.isBlocked(action)):
            reward = self.bad
        else:
            self.prevS=self.playerS
            self.playerS=self.takeAction(action)
            self.playerP = self.stateToPosition(self.playerS)
            self.playerGoesTo()
            if(self.playerS==24):
                reward = self.good
                self.done = True
            else:
                reward = self.ok
        
        return self.playerS, reward, self.done
            


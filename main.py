# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 11:55:00 2018

@author: Shashank
"""

import numpy as np
import time

from Environment1 import MazeEnv1


def trainQtable(Q,env,alpha,gamma,epsilon,epsilon_decay,max_epochs,verbose):
    for epoch in range(max_epochs):
        env.reset()
        state=env.playerS
        done = False
        k=0
        while not done:
            if np.random.rand() <= epsilon:
                l='random'
                action = np.random.randint(4)
            else:
                action = np.argmax(Q[state])
                l='from Q table'
            if(verbose):
                for dum in range(20):
                    print('\n')        
                print('Step {}, State {} (position{}) {},'.format(k,state,env.playerP,l))
    
            new_state, reward, done = env.step(action)
            
#            Q[state, action] += alpha * (reward + gamma * np.max(Q[new_state]) - Q[state, action])
            
            Q[state, action] = (reward + gamma * np.max(Q[new_state]))

            state = new_state
            k+=1
            if(verbose):
                env.render()
                time.sleep(0.25)
        print('Epoch {} took {} steps'.format(epoch,k))
        epsilon = epsilon * epsilon_decay
        if(verbose):
            time.sleep(2)
    print('\n Training Done!!')

def testQtable(Q,env,gamma):
    print('\n')
    print(Q)
    env.reset()
    state=env.playerS
    done = False
    k=1
    while not done:
        action = np.argmax(Q[state])
        print('\nStep{}) From state {}, the agent moves {} (value = {:.6f}).'.format(k,state,env.action_to_label[action],Q[state][action]))
        if(k>1):
            print('The immediate reward for the previous action was 0')
            print('The value of gamma is {}, and hence value of Vs (from the assignment question) is {:.6f}, which matches the value from step{}!!'.format(gamma,gamma*Q[state][action],k-1))
        print('Values for all possible actions are as follows:')
        print('up:{:.2f}\t down:{:.2f}\t left:{:.2f}\t right:{:.2f}'.format(Q[state][0],Q[state][1],Q[state][2],Q[state][3]))
        new_state, reward, done = env.step(action)
        state = new_state
        k+=1
        env.render()
        
    print('\n Testing Done!!')
            
def main():
    state_num=25
    action_num=4
    Q = np.random.rand(state_num, action_num)  # dimensions: states, actions
    
    alpha = 0.3  # learning rate, i.e. which fraction of the Q values should be updated
    gamma = 0.9  # discount factor, i.e. to which extent the algorithm considers possible future rewards
    epsilon = 0.3  # probability to choose random action instead of best action
    epsilon_decay = 0.9 #controls the rate of epsilon decay
    
    env = MazeEnv1([2,5,9,13,16,19]) #The numbers represent the positions of walls in the maze
    env.reset()
    
    max_epochs=25
    verbose=False
    
    trainQtable(Q,env,alpha,gamma,epsilon,epsilon_decay,max_epochs,verbose)
    testQtable(Q,env,gamma)
   

if __name__ == '__main__':
    main()
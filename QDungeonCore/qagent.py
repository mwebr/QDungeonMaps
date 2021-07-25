#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:43:49 2021

@author: marian
"""

import numpy as np

class QLearningAgent:
    # Final break up criteria
    treasure_check = False
    end_check = False

    def __init__(self, dungeon_map, gamma = 0.70, alpha = 0.85, q0_m = 1, q0_std = 0.1, debug = False):
        self.alpha = alpha # Learning rate alpha
        self.gamma = gamma # Discount factor gamma
        self.debug = debug # Show debug messages if True (e.g. current to next state)
        self.dungeon_map = dungeon_map
        self.n_states = pow(dungeon_map.fields_per_side, 2)
        
        # Initialize a Q_0 for primarily motivation of Q-learning algorithm with random noise
        self.Q = np.array(np.zeros([self.n_states, self.n_states])) \
                    + np.random.normal(q0_m, q0_std, (self.n_states, self.n_states)) 
        self.initRewards()
        
    def initRewards(self):
        # Initialize the rewards --> set all of them to one & priorize the treasure
        n_states = pow(self.dungeon_map.fields_per_side, 2)
        self.rewards = np.ones((n_states,n_states))
        self.rewards[self.dungeon_map.end_point, self.dungeon_map.end_point] = 0
        self.rewards[self.dungeon_map.treasure_point, self.dungeon_map.treasure_point] = 10
                
    def run(self):
        # Count necessary moves for comparisons
        necessary_moves = 0
        queue = np.array([])
        
        # While final condition not fulfilled (== treasure and end point found)
        while not(self.end_check and self.treasure_check): 
            # Get playable actions from current state (only move to neighbor fields)
            # This corresponds to a constraint in Q-learning process and exploration
            playable_actions = self.dungeon_map.get_playable_actions()
            
            # Q-Learning algorithm
            # Pick the most reasonable action from the list of playable actions  
            playable_q_values = np.array(
                [ self.Q [self.dungeon_map.current_point, i] for i in playable_actions])
            
            max_q_selection = np.argmax(playable_q_values)
            next_point = int(playable_actions[max_q_selection])
            
            if self.debug:
                print("Current state: %i, Subsequent state: %i, Q-value: %f" % 
                      (self.dungeon_map.current_point, next_point, np.max(playable_q_values)))
            
            #  Temporal difference calculation
            TD = self.rewards[self.dungeon_map.current_point, next_point] \
                + self.gamma * self.Q[next_point, np.argmax(self.Q[next_point, ])] \
                -  self.Q[self.dungeon_map.current_point, next_point]
            
        
            # Bellman equation --> update Q-values
            self.Q[self.dungeon_map.current_point, next_point] += self.alpha * TD
            
            if (self.debug):
                print("Updated Q-matrix:\n%s" % self.Q)
            
            # Update the rewards --> avoid going back (make a maze)
            # Penalty when QLearningAgent goes back to the state before --> enhance exploaration
            self.rewards[next_point, self.dungeon_map.current_point] = -10
            
            # Penalty (in the future) when QLearningAgent goes again to the new current state 
            self.rewards[:, next_point] = -10 
            
            # Move to map point (and break through wall)
            self.dungeon_map.move_to(next_point)

            queue = np.append(queue, next_point)
                
            
            # Verify if check points have been reached already
            if self.dungeon_map.current_point == self.dungeon_map.end_point:
                if (self.debug):
                    print("End point found")
                self.end_check = True

            if self.dungeon_map.current_point == self.dungeon_map.treasure_point:
                if (self.debug):
                    print("Treasure found")
                self.treasure_check = True
                # Reward for finding the end point
                self.rewards[self.dungeon_map.end_point, self.dungeon_map.end_point] = 10
                
                # We already found the treasure, so don't go there again
                self.rewards[self.dungeon_map.treasure_point, self.dungeon_map.treasure_point] = -1
                
            necessary_moves += 1
            
        return queue, necessary_moves
    
        if self.debug:
            print("Total number of agent's moves: %i" % necessary_moves)
            print("Queue / route: %s" % queue)
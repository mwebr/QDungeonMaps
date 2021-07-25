#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:37:15 2021

@author: marian
"""

import numpy as np
import matplotlib.pylab as plt
from matplotlib import colors


# TODO: adapt for non-quadratic maps
class DungeonMap:
    def __init__(self, fields_per_side = 4, start_point = 0, treasure_point = 9, end_point = 15):
        
        ## Initial values for map and actions
        self.fields_per_side = fields_per_side
        
        # Init map with all walls and spaces (0 = wall/corner, 1 = space) 
        self.maze_map = generate_new_default_map(fields_per_side)
        
        # Possible actions on this map (each field can be reached)
        self.actions = np.array(range(pow(fields_per_side, 2)))
        
        # Start, treasure and end point
        self.start_point = start_point
        self.treasure_point = treasure_point
        self.end_point = end_point
        
        # Place objects of interest on maze
        self.place_keypoints_on_maze()
        
        # Init marker
        self.current_point = start_point


    def move_to(self, next_point):
        # Calculate maze wall break position
        x = self.current_point % self.fields_per_side
        y = int(self.current_point  / self.fields_per_side)
        x_next = next_point % self.fields_per_side
        y_next = int(next_point / self.fields_per_side)
        
        x_move = x_next - x
        y_move = y_next - y
        
        pos_x = x * 2 + 1 + x_move
        pos_y = y * 2 + 1 + y_move
        
        # Break through wall
        self.maze_map[pos_x, pos_y] = 1 
        
        # Update current point
        self.current_point = next_point
        
        
    def place_keypoints_on_maze(self):
        for i in range(3):
            if i == 0:
                state = self.start_point
                value = 2
            elif i == 1:
                state = self.treasure_point
                value = 3
            elif i == 2:
                state = self.end_point
                value = 4
                    
            x = state % self.fields_per_side
            y = int(state / self.fields_per_side)
            pos_x = x * 2 + 1
            pos_y = y * 2 + 1
            self.maze_map[pos_x, pos_y] = value
            
    def get_playable_actions(self):
        state = self.current_point
        playable_actions = np.array([], dtype=np.int16)
        
         # Moving up in upper column not possible
        if not(state < self.fields_per_side):
            playable_actions = np.append(playable_actions, int(state - self.fields_per_side))
            
        # Moving down in lower column not possible
        if not(state >= pow(self.fields_per_side, 2) - self.fields_per_side): 
            playable_actions = np.append(playable_actions, int(state + self.fields_per_side))
            
        # Moving left (not possible when on left edge)
        if not(state % self.fields_per_side == 0): 
            playable_actions = np.append(playable_actions, int(state - 1))
            
        # Moving right (not possible when on right edge)
        if not((state+1) % self.fields_per_side == 0): 
            playable_actions = np.append(playable_actions, int(state + 1))
        return playable_actions
            
    def plot(self, title = 'Created map'):
        # Use own color map (blue = start, green = treasure, red = end)
        cmap = colors.ListedColormap(['black', 'white', 'blue', 'green', 'red'])
        bounds = [0,1,2,3,4,5]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        
        # Make a new plot
        plt.figure()
        plt.imshow(self.maze_map, interpolation='nearest', cmap=cmap, norm=norm)
        plt.axis('off')
        plt.title(title)
        
# static functions
def generate_new_default_map(fields_per_side = 4):
    fields_with_walls = fields_per_side * 2 + 1
    new_map = np.zeros((fields_with_walls, fields_with_walls))
    # Make empty boxes (between corners)
    for i in range(fields_per_side):
        for j in range(fields_per_side):
            new_map[i * 2 + 1, j * 2 + 1] = 1
    return new_map
    

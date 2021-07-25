from QDungeonCore.map_handler import DungeonMap
from QDungeonCore.qagent import QLearningAgent
import numpy as np

if __name__ == '__main__':
    
    # Example problem defintion as from task description (+ plot)
    # Here the default learning rate, discount factor, init Q mean + std have been used
    maze = DungeonMap(fields_per_side = 4, start_point = 0, treasure_point = 9, end_point = 15)
    agent = QLearningAgent(maze)
    agent.run()
    maze.plot('Original technical task description')
    
    # Examine Q-learning in terms of needed agent moves
    n_repetitions = 100
    moves_qlearning = np.zeros((n_repetitions))
    
    for i in range(n_repetitions):
        maze = DungeonMap(fields_per_side = 4, start_point = 0, treasure_point = 9, end_point = 15)
        agent = QLearningAgent(maze)
        _,moves_qlearning[i] = agent.run()
    
    print('In mean the Q-learning approach took %f moves to generate the maze' \
          % (np.mean(moves_qlearning)))
    
    # Some random examples for start, end and treasure points (+ plot)
    for i in range(5):
        #  Take random key points with np.random
        keys = np.random.choice(16, 3, replace=False)
        maze = DungeonMap(fields_per_side = 4, start_point = keys[0], treasure_point = keys[1], end_point = keys[2])
        agent = QLearningAgent(maze)
        
        agent.run()
        maze.plot('Random example no. %i' % i)
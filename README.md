# QDungeonMaps
QDungeonMaps is a small project to generate a random maze based on a Q-learning AI algorithm. The maze will be generated, so that there is a path from the starting point to the treasure, as well as to the end point.

## Deployment and test examples
Install all dependencies using the requirements.txt. As the project is currently very simple, only numpy for calculation and matplotlib for visualization are needed.

Change into the root project folder and for Anaconda use:
```shell
conda install --file requirements.txt
```

or with pip:
```shell
pip install -r requirements.txt
```

To start the test example execute test.py by running
```shell
python3 test.py
```

The main routine in the test program will first reproduce a comparable maze as given in the task description. In that use case the start, treasure and end point are predefined in a fixed position. The AI algorithm will then randomly create a maze around these check points - regarding the above path constraints. The resulting maze is displayed in the first figure with the title "Original technical task description".

Following that, the algorithm will be trained for 100 times to know how many moves are usually needed to create the maze. In comparison to a randomly generated maze (around 30 - 200 moves) the given AI based on Q-learning needs in mean around 30 moves to create the maze.

Lastly the AI will be trained 5 times with random check points (start, treasure, end) and plot the results into "Random example no. [0 ... 5]".

## Basic idea and architecture
The algorithm starts with a per default 4x4 maze where all walls are present (each cell contains 4 walls). The checkpoints "start point", "treasure point" and "end point" are placed on the map either per user definition or by random choice.

Then, the algorithm digs through the maze with a Q-learning agent starting from the start point. When it moves from one cell to another, the wall is removed and the maze is therefore formed gradually. The algorithm can only move from one cell to a neighboring cell. Everthing concerning the maze environment e.g. playable moves, tracking of the current position, checkpoints etc. is handled within QDungeonCore.map_handler. More specifically, each map is an instance of the DungeonMap class.

The Q-learning agent is an instance of the QLearningAgent class from the QDungeonCore.qagent module. It uses an instance of the DungeonMap class at initialization phase. 






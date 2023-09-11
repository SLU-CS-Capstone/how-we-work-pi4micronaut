from maze import Maze

seed = int(input("Provide seed: (leave empty for random seed)"))
maze = Maze(20, seed)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")

from q7 import *
t = tree(10, [tree(20), tree(30)])
apple = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
print_tree(village(apple, t))
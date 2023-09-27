from lab09 import Tree
def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    # >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    # >>> reverse_other(t)
    # >>> t
    # Tree(1, [Tree(4), Tree(3), Tree(2)])
    # >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    # >>> reverse_other(t)
    # >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    def get_num(depth,tree):
        if tree.is_leaf():
            return
        if depth %2 == 1:
            if len(tree.branches) > 1:
                tmp = []
                for b in tree.branches:
                    tmp.append(b.label)
                tmp.reverse()
                for i in range(len(tree.branches)):
                    tree.branches[i].label = tmp[i]
            else:
                return
        [get_num(depth + 1, b) for b in tree.branches]

    get_num(1,t)

t = Tree(1, [Tree(2), Tree(3), Tree(4)])
reverse_other(t)
print(t)
from Tree import Node, Tree

def negamax(n, h):
    score = -10000
    if n.is_leaf() or h == 0:

        return n.eval
    else:
        for daughter in n.daughters_reorder:
            t = -negamax(daughter, h - 1)
            score = max(t, score)

    return score

tree = Tree(3, 8, 100)
print(tree)

print(negamax(tree.root, 5))


import random


class Tree:
    def __init__(self, branching_factor, height, approximation):
        self.b = branching_factor
        self.h = height
        self.approx = approximation
        self.root = Node(random.randint(-2500, 2500), branching_factor, height, approximation)

    def __repr__(self):
        return str(self.root)

    def reset(self):
        self.root.reset()


class Node:
    def __init__(self, T, branching, height, approx):
        branches = branching
        rand = random.random()
        if rand > 0.95:
            branches = branching - 1
        elif rand > 0.9:
            branches = branching + 1

        self.daughters_original = []
        if height > 0 and T != 10000:
            for i in range(0, branches - 1):
                self.daughters_original.append(Node(random.randint(T, 10000), branching, height - 1, approx))

            self.daughters_original.insert(random.randint(0, len(self.daughters_original)),
                                           Node(random.randint(T, 10000), branching, height - 1, approx))

            self.daughters_reorder = self.daughters_original

            a = random.randint(-approx, approx)
            while T + a > 10000:
                a = random.randint(-approx, approx)

            self.eval = T + a
        else:
            self.eval = T

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.eval) + "\n"
        for child in self.daughters_original:
            ret += child.__repr__(level + 1)
        return ret

    def is_leaf(self):
        if self.daughters_original:
            return False
        return True

    def reset(self):
        self.daughters_reorder = self.daughters_original
        for daughter in self.daughters_reorder:
            daughter.reset()


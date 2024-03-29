"""
File: RegexTree.py
Author: Jackson Bates
Created: 6/3/2019 11:57 PM 
"""

class RegexTree:

    def __init__(self, name, children = None):
        self.name = name
        self.children = children

    def add_child(self, child_name):
        if self.children is None:
            self.children = [RegexTree(child_name)]
        else:
            self.children.append(RegexTree(child_name))

    def __repr__(self):
        return "RegexTree_"+self.name


def print_tree(tree, depth = 0):
    print(depth*'\t'+tree.name)
    if tree.children is not None:
        for child in tree.children:
            print_tree(child,depth+1)


if __name__ == '__main__':
    from random import randint
    root = RegexTree("Root")
    print_tree(root)
    for i in range(randint(4,30)):
        root.add_child("Child_{}".format(i))

    for child in root.children:
        for i in range(randint(5,20)):
            child.add_child("Grandchild_{}{}".format(child.name[-1],i))

    print_tree(root)






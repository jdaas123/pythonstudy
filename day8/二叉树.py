#!/usr/bin/python3
# author : jdaas
# 2026-01-28

class Node:
    def __init__(self, data,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.queue = []
    def add_node(self,node:Node):
        self.queue.append(node)
        self.size += 1
        if self.root is None:
            self.root = node
        else:
            if self.queue[0].lchild is None:
                self.queue[0].lchild = node
            else:
                self.queue[0].rchild = node
                self.queue.pop(0)
    def pre_order(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)
    def level_order(self):
        help_queue = []
        help_queue.append(self.root)
        while help_queue:
            node = help_queue.pop(0)
            print(node.data,end=" ")
            if node.lchild is not None:
                help_queue.append(node.lchild)
            if node.rchild is not None:
                help_queue.append(node.rchild)


if __name__ == '__main__':
    root = Tree()
    for i in range(1,11):
        node = Node(i)
        root.add_node(node)
    root.pre_order(root.root)
    print()
    root.level_order()



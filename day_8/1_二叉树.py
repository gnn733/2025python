# author:R
# 2026年01月04日11时40分51秒
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree:
    def __init__(self):
        self.root = None
        self.queue = []

    def level_build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.queue.append(node)
        else:
            self.queue.append(node)
            if self.queue[0].lchild is None:
                self.queue[0].lchild = node
            else:
                self.queue[0].rchild = node
                self.queue.pop(0)


def tree_print(root):
    if not root:
        return
    print(root.elem)
    tree_print(root.lchild)
    tree_print(root.rchild)


def level_order(root):
    queue= [root]
    while len(queue)>0:
        node=queue.pop(0)
        print(node.elem)
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)




if __name__ == '__main__':
    tree = BTree()
    for i in range(1, 10):
        new_node = Node(i)
        tree.level_build_tree(new_node)
    level_order(tree.root)

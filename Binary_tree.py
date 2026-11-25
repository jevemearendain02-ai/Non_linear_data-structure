# BINARY TREE PROGRAM - ARENDAIN
# Demonstrates Breadth-First Search (BFS) and Depth-First Search (DFS).
# Repeated letters are labeled A1, A2, N1, and N2 to distinguish them.

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_binary_tree():

    root = Node("A1")
    root.left = Node("R")
    root.right = Node("E")

    root.left.left = Node("N1")
    root.left.right = Node("D")

    root.right.left = Node("A2")
    root.right.right = Node("I")

    root.left.left.left = Node("N2")

    return root


def bfs(root):
    """Visit each level from left to right."""
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result


def dfs_preorder(root):
    """Visit Root, then Left subtree, then Right subtree."""
    if root is None:
        return []

    result = [root.value]
    result.extend(dfs_preorder(root.left))
    result.extend(dfs_preorder(root.right))
    return result


def print_tree(root, level=0, label="Root"):
    """Display the tree sideways in the console."""
    if root is not None:
        print_tree(root.right, level + 1, "R---")
        print("    " * level + label + " " + root.value)
        print_tree(root.left, level + 1, "L---")


def main():
    root = build_binary_tree()

    print("================================")
    print(" BINARY TREE - ARENDAIN")
    print("================================")
    print("\nTree structure (sideways view):")
    print_tree(root)

    print("\nBreadth-First Search (BFS):")
    print(" -> ".join(bfs(root)))

    print("\nDepth-First Search (DFS - Preorder):")
    print(" -> ".join(dfs_preorder(root)))


if __name__ == "__main__":
    main()

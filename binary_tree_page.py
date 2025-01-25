class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    @staticmethod
    def from_infix(expression):
        # Implementation for building a binary tree from an infix expression
        pass

    @staticmethod
    def from_postfix(expression):
        # Implementation for building a binary tree from a postfix expression
        pass

    @staticmethod
    def from_prefix(expression):
        # Implementation for building a binary tree from a prefix expression
        pass

    @staticmethod
    def in_order_traversal(node):
        if node is None:
            return []
        return BinaryTree.in_order_traversal(node.left) + [node.data] + BinaryTree.in_order_traversal(node.right)

    @staticmethod
    def pre_order_traversal(node):
        if node is None:
            return []
        return [node.data] + BinaryTree.pre_order_traversal(node.left) + BinaryTree.pre_order_traversal(node.right)

    @staticmethod
    def post_order_traversal(node):
        if node is None:
            return []
        return BinaryTree.post_order_traversal(node.left) + BinaryTree.post_order_traversal(node.right) + [node.data]


class BinaryTreeVisualizer:
    @staticmethod
    def tree_to_dict(node):
        if not node:
            return None
        return {
            'data': node.data,
            'left': BinaryTreeVisualizer.tree_to_dict(node.left),
            'right': BinaryTreeVisualizer.tree_to_dict(node.right)
        }

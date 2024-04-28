class DSATreeNode:
    def __init__(self, inKey, inValue):
        self._key = inKey
        self._value = inValue
        self._left = None
        self._right = None

    def __str__(self):
        return "Key: " + str(self._key) + " Value: " + str(self._value)

class DSABinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        self._root = self._insert_recursive(self._root, key, value)

    def _insert_recursive(self, root, key, value):
        if root is None:
            return DSATreeNode(key, value)
        if key < root._key:
            root._left = self._insert_recursive(root._left, key, value)
        elif key > root._key:
            root._right = self._insert_recursive(root._right, key, value)
        else:
            root._value = value
        return root

    def find(self, key):
        return self._find_recursive(self._root, key)

    def _find_recursive(self, root, key):
        if root is None or root._key == key:
            return root
        if key < root._key:
            return self._find_recursive(root._left, key)
        return self._find_recursive(root._right, key)

    def delete(self, key):
        self._root = self._delete_recursive(self._root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root._key:
            root._left = self._delete_recursive(root._left, key)
        elif key > root._key:
            root._right = self._delete_recursive(root._right, key)
        else:
            if root._left is None:
                temp = root._right
                root = None
                return temp
            elif root._right is None:
                temp = root._left
                root = None
                return temp
            temp = self._min_value_node(root._right)
            root._key = temp._key
            root._value = temp._value
            root._right = self._delete_recursive(root._right, temp._key)
        return root

    def _min_value_node(self, node):
        current = node
        while current._left is not None:
            current = current._left
        return current

    def min(self):
        if self._root is None:
            return None
        return self._min_recursive(self._root)._key

    def _min_recursive(self, root):
        if root._left is None:
            return root
        return self._min_recursive(root._left)

    def max(self):
        if self._root is None:
            return None
        return self._max_recursive(self._root)._key

    def _max_recursive(self, root):
        if root._right is None:
            return root
        return self._max_recursive(root._right)

    def height(self):
        return self._height_recursive(self._root)

    def _height_recursive(self, root):
        if root is None:
            return -1
        left_height = self._height_recursive(root._left)
        right_height = self._height_recursive(root._right)
        return max(left_height, right_height) + 1

    def balance(self):
        return self._balance_recursive(self._root)

    def _balance_recursive(self, root):
        if root is None:
            return 0
        left_height = self._height_recursive(root._left)
        right_height = self._height_recursive(root._right)
        return abs(left_height - right_height)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self._root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root._left, result)
            result.append(root._key)
            self._inorder_recursive(root._right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self._root, result)
        return result

    def _preorder_recursive(self, root, result):
        if root:
            result.append(root._key)
            self._preorder_recursive(root._left, result)
            self._preorder_recursive(root._right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self._root, result)
        return result

    def _postorder_recursive(self, root, result):
        if root:
            self._postorder_recursive(root._left, result)
            self._postorder_recursive(root._right, result)
            result.append(root._key)

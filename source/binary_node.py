
class BinaryNode(object):

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def is_internal(self):
        if self.left is not None or self.right is not None:
            return True
        else:
            return False

from asyncio.windows_events import NULL


class  Node:
    def __init__(self, input_data):
        self.data = input_data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root == None:
            return True
    def insert(self, data):
        pNew = Node(data)
        current = self.root
        prev = None
        if self.is_empty():
            self.root = pNew
        else:
            while current != None:
                if data < current.data:
                    prev = current
                    current = current.left
                else:
                    prev = current
                    current = current.right
            if data < prev.data:
                prev.left = pNew
            else:
                prev.right = pNew

        return self
        
    def preorder(self, root):
        if root != None:
            print ("->", root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print("->", root.data, end=" ")
            self.inorder(root.right)
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        if self.is_empty():
            print("Error: Tree is empty")
        else:
            print("\nPreorder:")
            self.preorder(self.root)
            print("\nInorder:")
            self.inorder(self.root)
            print("\nPostorder:")
            self.postorder(self.root)
    def findMin(self):
        current = self.root
        while current.left != None:
            current = current.left
        return current.data
    def findMax(self):
        current = self.root
        while current.right != None:
            current = current.right
        return current.data

    def delete(self, data):
        current = self.root
        prev = None
        if self.is_empty():
            print("can't delete")
        else:
            while current.data != data:
                if data < current.data:
                    prev = current
                    current = current.left
                else:
                    prev = current
                    current = current.right
                    
            if current.left == None and current.right == None:
                if prev.left == current:
                    prev.left = None
                else:
                    prev.right = None
            elif current.left != None and current.right == None:
                if prev.left == current:
                    prev.left = current.left
                else:
                    prev.right = current.left
            elif current.left == None and current.right != None:
                if prev.left == current:
                    prev.left = current.right
                else:
                    prev.right = current.right
            # elif current.left == None and current.right == None:
            #     c2 = self.root
            #     p2 = None
            #     while c2.data != None:
            #         if data < c2.data:
            #             p2 = c2
            #             c2 = c2.left
            #     if prev.left == current:
            #         prev.left = p2
            #         del p2

myBST = BST()
myBST.insert(14); 
myBST.insert(23)
myBST.insert(7); myBST.insert(10)
myBST.insert(33); myBST.insert(5)
myBST.insert(20); myBST.insert(13)
myBST.traverse()
myBST.delete(5)
myBST.traverse()
myBST.delete(33)
myBST.traverse()
myBST.delete(7)
myBST.traverse()
myBST.delete(23)
myBST.traverse()

print("\nMax : ", myBST.findMax())
print("Min : ", myBST.findMin())

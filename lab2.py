class DataNode:
    def __init__(self, input_name):
        self.name = input_name
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    
    def traverse(self):
        if self.head == None:#empty lst
            print("empty list")
        else:
            pos = self.head
            while pos != None:
                print("->", pos.name, end = " ")
                pos = pos.next
            print("")
        return

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1
        return

    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pos = self.head
            while pos.next != None:
                pos = pos.next
            pos.next = pNew
        self.count += 1
        return
    
    def insertBefore(self, node, data):
        pNew = DataNode(data)
        if self.head == None:
            print("Cannot insert")
        else:
            pos = self.head
            prev = None
            if pos.name == node:
                pNew.next = self.head
                self.head = pNew
            else:
                while pos != None:
                    if pos.name == node:
                        pNew.next = pos
                        prev.next = pNew
                        break
                    prev = pos
                    pos = pos.next 
                if pos == None:
                    print("Not found")
        self.count += 1
        return

    def delete(self, data):
        if self.head == None:
            print("cannot delete")
        else:
            pos = self.head
            prev = None
            if pos.name == data:
                self.head = pos.next
            else:
                while pos.name != data:
                    prev = pos
                    pos = pos.next
                    break
                prev.next = pos.next
        return

        

mylist = SinglyLinkedList()
pNew = DataNode("John")
mylist.head = pNew
print(mylist.head.name)
pNew = DataNode("Tony")
mylist.head.next = pNew
print(mylist.head.next.name)

pNew = DataNode("Bill")
mylist.head.next.next = pNew
mylist.traverse()

mylist.insertFront("Kim")
mylist.traverse()

mylist.insertLast("Yuy")
mylist.traverse()

mylist.insertBefore("Kim", "Tom")
mylist.traverse()

mylist.delete("Tom")
mylist.traverse()
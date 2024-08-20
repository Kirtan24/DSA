class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # Insert at First
    def insertAtFisrt(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        print("\nInserted...")
        
    # Insert at Last
    def insertAtLast(self,data):
        new_node = Node(data)
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        print("\nInserted...")
            
    # Insert at Specific Index
    
    # def insertAtIdx(self,idx,data):
    #     if idx < 0 or idx >= self.count:
    #         print("Invalid Location Entered!")
    #     elif idx == 0:
    #         self.insertAtFisrt(data)
    #     elif idx == self.count:
    #         self.insertAtLast(data)
    #     else:
    #         new_node = Node(data)
    #         n = self.head
    #         for _ in range(idx - 1):
    #             n = n.next
    #         new_node.next = n.next
    #         new_node.prev = n
    #         n.next.prev = new_node
    #         n.next = new_node
    #         self.count =+ 1
    #         print("\nInserted...")
    
    def insertAtIdx(self, idx, data):
        if idx < 0 or idx > self.count:
            print("Invalid Location Entered!")
            return
        
        new_node = Node(data)
        
        if idx == 0:
            self.insertAtBeginning(data)
        elif idx == self.count:
            self.insertAtEnd(data)
        else:
            if idx < self.count // 2:
                # Traverse from the head
                n = self.head
                for _ in range(idx - 1):
                    n = n.next
                new_node.next = n.next
                new_node.prev = n
                n.next.prev = new_node
                n.next = new_node
            else:
                # Traverse from the tail
                n = self.tail
                for _ in range(self.count - idx):
                    n = n.prev
                new_node.prev = n
                new_node.next = n.next
                n.next.prev = new_node
                n.next = new_node
            
            self.count += 1
            print("\nInserted...")
            
    # Update
    def update(self,idx,data):
        if self.head == None:
            print("Linked List is Empty!")
        elif idx < 0 or idx > self.count:
            print("Invalid Location Entered!")
        else:
            if idx < self.count // 2:
                # Traverse from the head
                n = self.head
                for _ in range(idx - 1):
                    n = n.next
                print(f"Old Value : {n.data}")
                n.data = data
                print(f"New Value : {n.data}")
            else:
                # Traverse from the tail
                n = self.tail
                for _ in range(self.count - idx):
                    n = n.prev
                print(f"Old Value : {n.data}")
                n.data = data
                print(f"New Value : {n.data}")
            print("\nUpdated...")
    
    # Delete First
    def deleteFirst(self):
        if self.head == None:
            print("List is Empty!")
        else:
            print(f"{self.head.data} is Deleted.")
            self.head = self.head.next
            self.count -= 1
            
    def empty(self,head):
        print(f"{head.data} is Deleted.")
        self.head = None
        self.tail = None
        self.count -= 1
            
    # Delete Last
    def deleteLast(self):
        if self.head == None:
            print("List is Empty!")
        elif self.head == self.tail:
            self.empty(self.head)
        else:
            n = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            print(f"{n.data} is Deleted.")
            self.count -= 1
    
    # Delete At Specific Index
    def deleteAtIdx(self,idx):
        if self.head == None:
            print("List is Empty!")
        elif self.head == self.tail:
            self.empty()
        elif idx - 1 == 0:
            self.deleteFirst()
        elif idx - 1 == self.count:
            self.deleteLast()
        else:
            if idx < self.count // 2:
                n = self.head
                for _ in range(idx):
                    n = n.next
            else:
                n = self.tail
                for _ in range(self.count - idx - 1):
                    n = n.prev
            n.prev.next = n.next
            n.next.prev = n.prev
            print(f"{n.data} is Deleted.")
    
    # Display
    def display(self):
        if self.head == None:
            print("\nLinked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data}",end=" ")
                n = n.next
    
    # Display Reverse
    def displayReverse(self):
        if self.head == None:
            print("\nLinked List is Empty!")
        else:
            n = self.tail
            while n is not None:
                print(f"{n.data}",end=" ")
                n = n.prev
                
# Main Function
ll = LinkedList()
while True:
    print("\nLinked List Operations\n")
    print("1) Insert")
    print("2) Update")
    print("3) Delete")
    print("4) Display")
    print("5) Display Reverce")
    print("0) Exit")
    c = int(input("Enter the Choice : "))
  
    if c == 1:
        while True:
            print("\nInsert Operations\n")
            print("1. Insert At First")
            print("2. Insert At Last")
            print("3. Insert At Specific Location")
            print("0. Exit")
            c2 = int(input("Enter the Choice : "))
    
            if c2 == 1:
                data = int(input("Enter Data : "))
                ll.insertAtFisrt(data)
                    
            elif c2 == 2:  
                data = int(input("Enter Data : "))
                ll.insertAtLast(data)
                    
            elif c2 == 3:  
                idx =  int(input("Enter Location (0-Based Index) : "))
                data = int(input("Enter Data : "))
                ll.insertAtIdx(idx,data)

            elif c2 == 0:  
                break

            else:  
                print("Oops! Incorrect Choice.")  
        
    elif c == 2:  
        idx =  int(input("Enter Location (0-Based Index) : "))
        data = int(input("Enter New Data : "))
        ll.update(idx,data)
        
    elif c == 3:
        while True:
            print("\nDelete Operations\n")
            print("1. Delete First")
            print("2. Delete Last")
            print("3. Delete Specific Location")
            print("0. Exit")
            c3 = int(input("Enter the Choice : "))

            if c3 == 1:
                ll.deleteFirst()
                    
            elif c3 == 2:  
                ll.deleteLast()
                    
            elif c3 == 3:  
                idx =  int(input("Enter Location (0-Based Index) : "))
                ll.deleteAtIdx(idx)

            elif c3 == 0:
                break

            else:  
                print("Oops! Incorrect Choice.")
            
    elif c == 4:
        ll.display()
        print()
        
    elif c == 5:
        ll.displayReverse()
        print()
        
    elif c == 0:
        break

    else:
        print("Oops! Incorrect Choice.")
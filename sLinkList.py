count = 0
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    # Insert at First
    def insertAtFisrt(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("\nInserted...")
        global count
        count = count + 1
        
    # Insert at Last
    def insertAtLast(self,data):
        new_node = Node(data)
                
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print("\nInserted...")
        global count
        count = count + 1
            
        # if self.head == None:
        #     self.insertAtFisrt(data)
        # else:
        #     n = self.head
        #     while n.next is not None:
        #         n = n.next
        #     n.next = new_node
            
    # Insert at Specific Index
    def insertAtIdx(self,idx,data):
        new_node = Node(data)
        global count
        if idx < 0 or idx >= count:
            print("Invalid Location Entered!")
        elif self.head == None or idx == 0:
            self.insertAtFisrt(data)
        elif idx == count-1:
            self.insertAtLast(data)
        else:
            c = 0
            n = self.head
            while n is not None:
                if c == idx-1:
                    new_node.next = n.next
                    n.next = new_node
                    break
                n = n.next
                c += 1 
            print("\nInserted...")
            count = count + 1
            
    # Update
    def update(self,idx,data):
        global count
        if idx < 0 or idx >= count:
            print("Invalid Location Entered!")
        elif self.head == None:
            print("Linked List is Empty!")
        else:
            c = 0
            n = self.head
            while n is not None:
                if idx == c:
                    print(f"Old Value : {n.data}")
                    n.data = data
                    print(f"New Value : {n.data}")
                n = n.next
                c += 1
            print("\nUpdated...")
    
    # Delete First
    def deleteFirst(self):
        if self.head == None:
            print("List is Empty!")
        else:
            global count
            print(f"{self.head.data} is Deleted.")
            self.head = self.head.next
            count -= 1
            
    # Delete Last
    def deleteLast(self):
        global count
        if self.head == None:
            print("List is Empty!")
        elif count == 1:
            self.deleteFirst()
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
            count -= 1
    
    # Delete At Specific Index
    def deleteAtIdx(self,idx):
        global count
        if self.head == None:
            print("List is Empty!")
        elif count == 1:
            self.deleteFirst()
        elif idx - 1 == count:
            self.deleteLast()
        else:
            n = self.head
            for _ in range(idx - 1):
                if n is None:
                    print("Index out of bounds.")
                    return
                n = n.next
            if n is None or n.next is None:
                print("Index out of bounds.")
                return
            n.next = n.next.next
            count -= 1
        return
    
    # Display
    def display(self):
        if self.head == None:
            print("\nLinked List is Empty!")
        else:
            n = self.head
            print(f"Total Elements : {count}")
            while n is not None:
                print(f"{n.data}",end=" ")
                n = n.next
                
# Main Function
ll = LinkedList()
while True:
    print("\nLinked List Operations\n")
    print("1) Insert")
    print("2) Update")
    print("3) Delete")
    print("4) Display")
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
        
    elif c == 0:
        break

    else:
        print("Oops! Incorrect Choice.")
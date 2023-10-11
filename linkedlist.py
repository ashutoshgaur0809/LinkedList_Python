class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.start = None
    def insertLast(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    def insertFirst(self,value):
        newNode = Node(value)
        newNode.next = self.start
        self.start = newNode  
    def inserti(self,i,value):
        newNode = Node(value)
        temp = self.start
        for i in range(i -1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        
    def deli(self,i):
        pre = self.start
        temp = self.start.next
        for i in range(i-1):
            temp = temp.next
            pre = pre.next
        pre.next = temp.next       
                      
    def delFirst(self):
        if self.start == None:
            print("Empty LL")
        else:
            self.start = self.start.next
            
    def delLast(self):
        pre = self.start
        temp = self.start.next
        while temp.next!=None:
            temp = temp.next
            pre = pre.next
        pre.next = None    
                
    def view(self):
        if self.start == None:
            print("Empty LL")
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next
                
a = LL()
while(True):
    print("Enter Options ==> ")
    print("1.Insert At Start \n2.Insert At last \n3.insert at I index\n")
    print("4.del At Start \n5.del At last \n6.del at I index\n")
    print("7.View")
    ch = int(input())
    if ch == 1:
        a.insertFirst(int(input("Enter Value You want to insert at first-->")))
    elif ch == 2:
         a.insertLast(int(input("Enter Value You want to insert at Last-->")))   
    elif ch == 3:
        a.inserti(int(input("Enter index-->")),int(input("Enter No.-->")))     
    elif ch == 4:
        a.delFirst()
    elif ch == 5:
         a.delLast 
    elif ch == 6:
        a.deli(int(input("Enter index-->")))     
    else:
        a.view()    

                                                   
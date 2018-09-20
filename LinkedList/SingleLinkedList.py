class Node:
	def __init__(self, data): 
		self.data = data
		self.next = None  

class LinkedList:
	def __init__(self):
		self.head = None

	def InsertFirst(self,item):
		newNode=Node(item) 
		newNode.next=self.head
		self.head=newNode
	
	def InsertLast(self,item):
		



if __name__=='__main__':

	linkedList = LinkedList()

	while(True):
		print("Enter the choice \n 1.Insert 2. Delete 3. Traverse 4.Exit")
		choice=int(input())
		if choice == 1:
			while(True):
				print("Enter the choice \n 1.InsertFirst 2.InsertLast 3.InsertAfter 4.Exit")
				choice=int(input())
				if choice == 1:
					linkedList.InsertFirst(int(input("Enter the Value to be inserted")))
				elif choice ==2:
					linkedList.InsertLast()
				elif choice == 3:
					InsertAfter()
				else:
					break
		elif choice ==2:
			Delete()
		elif choice == 3:
			Traverse()
		else:
			break

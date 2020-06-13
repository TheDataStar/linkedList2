# Project: Linked List 2
# Author: Adam A.G
# Date: June, 2020
# Purpose: 
#   CS233T Unit 2 Submission 1, Linked List 2 in "Python".
#   Create a structure as a studentnode that has data and pointer to next
#   Create a constructor to initialize the linked list
#   Implement a destructor to clear data once executed
#   Implement a function to add a new node into the list with value
#   Write a method to print all the values

# Node class, that stores data with a single pointer to next.
class Node:
    # Constructor
    def __init__(self, data, next):
        self.data = data
        self.next = None

    # Destructor
    def __del__(self):
        print("Program End : Memory Cleared")

# Linked List class creation, head node.
class linkedList:
    def __init__(self):
        self.head = None

    # List Manipulation methods
    def insert(self, data):
        newNode = Node(data, next)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # List print method
    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

studentNode = linkedList()
studentNode.insert("student1")
studentNode.insert("student2")
studentNode.insert("student3")
studentNode.insert("student4")
studentNode.printList()


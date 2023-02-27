### Fill-up step-by-step the class Heap to address the question below
class Heap:

  def __init__(self):
    self.__heap=[]

  def size(self):
    return len(self.__heap)
  
  def insert(self,data):
    self.__heap.append(data)
    self.trickleUp(self.size()-1)
    
  def isEmpty(self):
    return self.size()==0
  
  def remove(self):
    if self.isEmpty(): return None
    root=self.__heap[0]
    node=self.__heap.pop() #reduce size by 1
    if self.size()>0:
      self.__heap[0]=node
      self.trickleDown(0)
    return root

  def trickleUp(self,index):
    #reach top of heap - done
    if index==0: return
    #check if parent is smaller
    parent=(index-1)//2
    if self.__heap[index]<self.__heap[parent]:
      #swap
      temp =self.__heap[index]
      self.__heap[index]=self.__heap[parent]
      self.__heap[parent]=temp
      self.trickleUp(parent) #recursion

  def trickleDown(self,index):
    leftChild=2*index+1
    rightChild=leftChild+1
    # index is a leaf node- done
    if leftChild>=self.size(): return
    # index has only a left child
    if rightChild>=self.size():	
     if self.__heap[index]>self.__heap[leftChild]:  
      #swap
      temp =self.__heap[index]
      self.__heap[index]=self.__heap[leftChild]
      self.__heap[leftChild]=temp
     return
    #index has two children
    if self.__heap[index]>self.__heap[leftChild] or self.__heap[index]>self.__heap[rightChild]:	
 	    #need to continue trickling down	
      if self.__heap[leftChild]<self.__heap[rightChild]: 
        #swap with left child	
        temp =self.__heap[index]
        self.__heap[index]=self.__heap[leftChild]
        self.__heap[leftChild]=temp
        self.trickleDown(leftChild) #recursion
      else:
        #swap with right child	
        temp =self.__heap[index]
        self.__heap[index]=self.__heap[rightChild]
        self.__heap[rightChild]=temp
        self.trickleDown(rightChild) #recursion

  def display(self):
    for i in self.__heap:
      print(i,end=" ")
    print()

  def show(self):
        print("The Heap looks like: ")
        self.__recShow(0,"")

  def __recShow(self,index,indentStr):
        if index<self.size():
            self.__recShow(index*2+2,indentStr+"      ")
            print(indentStr+str(self.__heap[index]))
            self.__recShow(index*2+1,indentStr+"      ")

### Your NAMES: Connor McGarry
###

from tkinter import *
from Stack import *
from Queue import *
from Heap import *
import sys

'''Type vertex that stores coordinates of the nodes in the graoh'''
class Vertex:
    def __init__(self,i,j):
        self.x = i
        self.y = j
        self.value = (i,j)  # sets a tuple of the x y coordinates
        self.visited = False

    def __str__(self):
        return "(%s, %s)"%(self.x,self.y)


'''Type edge that stores 2 connectning nodes, and the weight of the connection. Also overloads the < and > operators to compare weight of edges'''
class Edge:
    def __init__(self,start,end,weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "<%s%s%s>"%(self.start,self.end,self.weight)

    def __lt__(self,compare):
        if self.weight < compare.weight:
            return True 
        return False

    def __gt__(self,compare):
        if self.weight > compare.weight:
            return True
        return False


'''Type graph that initiaites nodes and a matrix of 0's'''
class Graph:
    def __init__(self,nx,ny):  # takes size of the graph
        self.nx = nx   # legnth
        self.ny = ny  # height
        self.maxnodes = nx*ny  # size of one row of the matrix
        self.vertices=[] #list of Vertex
        self.matrix=[] #adj. 2D Matrix, is a list of lists
        for i in range(self.maxnodes):
            self.matrix.append([0]*self.maxnodes)  # rows and columns of 0s corrosponding to the amount of total nodes
        for i in range(self.ny):
            for j in range(self.nx):
                self.vertices.append(Vertex(j,i))  # appends vertex object as nodes for the graph, data corrosponds to the size of the graph


    '''accepts 2 nodes and the weight of the connection, (1 by default), and adds the weight to the corrosponding area in the matrix'''
    def addEdge(self,node1,node2,weight=1):   # takes in 
        i1,i2=None,None
        for i in range(len(self.vertices)):
            node=self.vertices[i]
            if node.value==node1: i1=i
            if node.value==node2: i2=i
        if (i1 is not None) and (i2 is not None):
            self.matrix[i1][i2] = weight  # sets the connection between vertices to the value of the given weight 
            self.matrix[i2][i1] = weight


    '''automatically adds the edges to a given size of a matrix under certain constraints '''
    def form2DGrid(self):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    node1 = self.vertices[i]
                    node2 = self.vertices[j]
                    if (node1.x  + 1 ==  node2.x) and (node1.y == node2.y): # if the x coords  are next to eachoter and the y nodes are equal 
                        self.addEdge(node1.value,node2.value)
                    elif (node1.y + 1  ==  node2.y) and (node1.x == node2.x): # if the y coords are next to eachother and the x nodes are equal 
                        self.addEdge(node1.value,node2.value)


    '''prints out information regarding the node connections and the weight of the edge connecting them '''
    def displayInfoGraph(self):
        temp= [] # track repeating connections
        sum = 0  # track the total weight of the edges
        print('\nList of edges + weights:',end='\n')
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.matrix[i][j]!=0:  # if the weight of the edge in the matrix is not 0
                    if not ((self.vertices[j],self.vertices[i])) in temp:  # if the reverse of the connection has not already been printed
                        print(self.vertices[i],"<==>",self.vertices[j],self.matrix[i][j])  # print the connection and the weight of the edge 
                        temp.append((self.vertices[i],self.vertices[j]))  # appebd the tuple to a list to track its printing
                        sum += self.matrix[i][j]  # add weight to total   
        print('Total weight: %s '%(sum))


    '''prints the adjacency matrix, which is a list of lists, in a column form'''
    def displayAdjMat(self):
        print("\nMatrix: ")
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                print(self.matrix[i][j],end=" ")
            print()


    '''retuens the number of nods in the graph'''
    def getnVertex(self):
        return len(self.vertices)


    '''performs depth first search on the graph and adds corrosponding edges to visited nodes. Uses a Stack'''
    def dfs(self,start):
        self.vertices[start].visited=True # making sure to keep track if the nodes have been visited
        dfs = Graph(self.nx,self.ny)
        mystack=Stack()
        mystack.push(start)
        while not mystack.isEmpty():
            current = mystack.peek() 
            j=self.getAdjUnvisitedNode(current)  # look for the vertex that is adjacent to the current one 
            if j is None:
                mystack.pop() # if there is none then remove the current one 
            else:
                dfs.addEdge(dfs.vertices[j].value,dfs.vertices[current].value,self.matrix[current][j])  # add an edge between current node and its adjacent 
                self.vertices[j].visited=True
                mystack.push(j) 

        for n in self.vertices: n.visited=False # reset the flags for visited
        return dfs # return a new Graph()


    'performs breadth first search and adds edges to to the visited nodes. Uses a Queue'
    def bfs(self,start):
        bfs = Graph(self.nx,self.ny)
        self.vertices[start].visited=True
        myqueue=Queue()
        myqueue.enqueue(start)
        while not myqueue.isEmpty():
            k=myqueue.dequeue()  # get value from the queue
            while True:
                j=self.getAdjUnvisitedNode(k)  # check is there is a node next to the current one 
                if j is None: break
                bfs.addEdge(bfs.vertices[k].value,bfs.vertices[j].value,self.matrix[j][k])  # add an edge between current and adjacent node
                self.vertices[j].visited=True
                myqueue.enqueue(j)


        for n in self.vertices: n.visited=False  # reset the flags
        return bfs  # returns a new Graph()


    '''checks if a file exists, and if so, puts the supplied vertices and edge weights into matrix '''
    def load2DGrid(self,filename):
        try: f = open(filename,'r')
        except: 
            print('File does not exist')
            sys.exit(0)

        lines = f.readlines() # reads through the movies
        for l in lines:   
            n = l.strip('\n').split(' ')  # makes the data into a list 
            self.addEdge(self.vertices[int(n[0])].value,self.vertices[int(n[1])].value,int(n[2]))  # add edge with values in the list of data lines 


    '''searches for the minumum cost path throughout the data considering the weights of the edges. Uses the Edge() class and a Heap acting as a priority queue'''

    '''***********************************I was unable to figure out how to implement this*******************'''
    def mstw(self,start):
        print('****************code incomplete, my apologies******************')
        sys.exit(0)
    '''def mstw(self,start):

        mstw = Graph(self.nx,self.ny)
        self.vertices[start].visited=True
        myheap=Heap()
        next = self.getAdjUnvisitedNode(start)
        myheap.insert(Edge(start,next,))    I know it is some sort of loop regarding inserting edges and checking the minimum adjacent node 
        
        for i in range(len(self.vertices)):
            next = self.getAdjUnvisitedNode(start)
            if next == None: break
            #ins = myheap.insert(Edge(start,next,int(0)))
            self.vertices[next].visited = True
            for j in range(len(self.vertices)):
                if self.matrix[next][j] != 0 and self.vertices[j].visited == False and edge.weight > self.matrix[next][j]:
                    edge weight = self.matrix[next][j]

        return mstw'''


    '''returns the adjacent node in the matrix of the input '''
    def getAdjUnvisitedNode(self,v):
        for i in range(len(self.vertices)):
            if (self.matrix[v][i]!=0) and (self.vertices[i].visited==False):
                return i # found neighbor
        return None #no such node


    '''plots the verteces and edges by taking the weights and locations from the matrix and nodes'''
    def plot(self,color):
        root = Tk()
        w = 80*self.nx
        h = 80*self.ny  # adjusting canvas size
        canvas = Canvas(root, width=w,height=h,bg='white')
        canvas.pack()

        for i in range(len(self.vertices)):
            x,y=Graph.toTkinter(self.vertices[i].x,self.vertices[i].y,-1,self.nx,-1,self.ny,w,h)
            canvas.create_oval(x-10,y-10,x+10,y+10,fill=color) # ovals of radius 10

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.matrix[i][j] != 0:  # only if the weights are not 0 meaning that there is an edge 
                    x,y=Graph.toTkinter(self.vertices[i].x,self.vertices[i].y,-1,self.nx,-1,self.ny,w,h)   # start coords
                    a,b=Graph.toTkinter(self.vertices[j].x,self.vertices[j].y,-1,self.nx,-1,self.ny,w,h)  # end coords
                    canvas.create_line(x,y,a,b,width=3*self.matrix[i][j],fill=color)  # create a line of the weight in the matrix between generated start and end coords/vertices 
                
        root.mainloop()


    '''helper method to convert coordinates into Tkinter specific coordinates'''
    @ staticmethod
    def toTkinter(x,y,xmin,xmax,ymin,ymax,width,height):
        i = int((x-xmin)*(width)/(xmax-xmin))
        j = int((ymax-y)*(height)/(ymax-ymin))
        return i,j

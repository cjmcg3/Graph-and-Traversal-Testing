from Graph import *

print("\nWelcome to Graph App 3")
print("========================\n")


#Generate a Graph using a 2D Grid
nx,ny=map(int,input("Enter Total Grid Size Nx and Ny: ").split())

mygraph=Graph(nx,ny) #instantiate Graph using all weights to zero by default

#Read Graph connections from File
filename="grid"+str(nx)+"x"+str(ny)+".txt"
mygraph.load2DGrid(filename)
mygraph.displayInfoGraph()

# if Nvertex<=9, display the matrix
if mygraph.getnVertex()<=9: mygraph.displayAdjMat()

#Plot the main graph
#mygraph.plot("gray")


#Perform DFS, BFS or MSTW and create a new MST graph
choice=int(input("\nPerform: 1-DFS,  2-BFS or  3-MSTW? "))
node=int(input("Choose the starting node number: "))

if choice==1:
    mstgraph=mygraph.dfs(node)
elif choice==2:
    mstgraph=mygraph.bfs(node)
elif choice==3:
    mstgraph=mygraph.mstw(node)

#Display new  graph info and plot    
mstgraph.displayInfoGraph()
mstgraph.plot("blue")


""" 
while True:
    command=input("\nHow do you want to generate the MSTree? (1:DFS, 2:BFS, 3:MSTW or Press Enter to Exit): ")
    if command=="": break
    command=int(command)
    if (command==1 or command==2):
        node=int(input("\nEnter the starting node number to start the search: "))
        
    if command==1:
        mst=mygraph.dfs(node) # call DFS algo
    elif command==2:
        mst=mygraph.bfs(node) # call BFS algo
    elif command==3:  mst=mygraph.mstw() # minimum spanning tree

    ## some info/output
    mst.displayInfoGraph()
    mst.plot("BLUE")
"""	    

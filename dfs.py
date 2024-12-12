def Graph(num):
    childcity=[]
    for i in range(num):
        city=input("Enter city")
        numchild=int(input("Enter no of child city"))
        lchild=[]
        for n in range(numchild):
            lchild.append(input("Enter child city"))
        childcity.append(lchild)
        graph[city]=childcity[i]
def DFS(graph,node,goal):
    visited=[]
    stack=[]
    visited.append(node)
    stack.append(node)
    while stack:
        node=stack.pop()
        print(node)
        if (node==goal):
            print(node)
            break

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                stack.append(i)
visited=[]
stack=[]
graph={}
num=int(input("enter the number of cities in the graph: "))
Graph(num)
print("the graph is: ")
print(graph)

start=input("Enter the start city: ")
destination=input("Enter the destination city: ")

print("The path to the destination is: ")
dfs(visited,graph,start,destination)

graph={}
def Graph(num):
    child=[]
    for i in range(num):
        city=input("Enter city")
        noc=int(input("Enter no of children city"))
        lchild=[]
        for j in range(noc):
            lchild.append(input("Enter child city"))
        child.append(lchild)
        graph[city]=child[i]
def bfs(graph,node,goal):
    visit=[]
    q=[]
    visit.append(node)
    q.append(node)
    while q:
        node=q.pop(0)
        print(node)
        if (node==goal):
            print(node)
        for i in graph[node]:
            if i not in visit:
                visit.append(i)
                q.append(i)
num=int(input("Enter no of cities"))
Graph(num)
start=input("start:")
end=input("end:")
print("The path :")
bfs(graph,start,end)


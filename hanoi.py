def toh(n , start, end, aux): 
    if n == 1: 
        print ("move disk 1 from pole",start,"to pole",end)
        return
    toh(n-1, start, aux, end) 
    print ("move disk",n,"from pole",start,"to pole",end)
    toh(n-1, aux, start, end) 
           
n = int(input('enter the no. of disks: '))
toh(n, 'C', 'B', 'A')

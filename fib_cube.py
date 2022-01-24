cube = lambda x:x*x*x

def fibonacci(n):
    num=[0,1]
    if(n==0):
        return([])
    elif(n==1):
        return([0])
    elif(n==2):
        return([0,1])
    for i in range(1,n-1):
        x=num[i]+num[i-1]  
        num.append(x)  
    return(num)

if __name__ == '__main__':
    n = int(input("Enter Number "))
    print(list(map(cube, fibonacci(n))))

class solution():
    def pattern(n):
        row=1
        while(row<=n):
           #print space(1st triangle)
            space = n-row
            while(space):
                print(" ",end="")
                space-=1

           #print 2nd triangle
            col=1
            while(col<=row):
                print(col,end="")
                col+=1
            # print()

           #print 3rd triangle 
            start = row -1
            while(start):
                print(start,end = "")
                start-=1
            print()
            row+=1

if __name__ == '__main__':
    ob = solution
    num = int (input("Enter Number = "))
    ob.pattern(num)
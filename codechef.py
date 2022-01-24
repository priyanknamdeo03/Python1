
def Elections(A,B,C):
    if (A >= 50):
        print("A")
    elif (B >= 50):
        print("B")
    elif (C >= 50):
        print("C")
    else:
        print("NOTA")

if __name__ == "__main__":
    try:
        T = int(input())
        while(T > 0):
            A = int(input())
            B = int(input())
            C = int(input())
            Elections(A, B, C)
            T = T-1
    except:
        pass
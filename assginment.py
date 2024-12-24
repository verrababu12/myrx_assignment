numbers=list(map(int,input().split()))

squares=[]

for i in numbers:
    square_of_each_num=i**2
    squares.append(square_of_each_num)
res=sorted(squares)  
print(res)
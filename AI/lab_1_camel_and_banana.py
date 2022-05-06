total=int(input('Enter no. of bananas at starting point:'))
distance=int(input('Enter distance you to be covered:'))
max_capacity=int(input('Max. Capacity of camel:'))
lose=0
start_point=total
for i in range(distance):
    while start_point>0:
        start_point=start_point-max_capacity
        if start_point==1:
            lose=lose-1
        lose=lose+2

    lose=lose-1
    start_point=total-lose
    if start_point==0:
        break
print(start_point)
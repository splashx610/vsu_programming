x = float(input("x = "))
y = float(input("y = "))
if x > 0 and y > 0:
    print('первая четверть')
elif x < 0 and y < 0:
    print('третья четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif  x < 0 and y > 0:
    print('2 четверть')
else:
    print("на оси") 

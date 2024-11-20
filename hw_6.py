
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    print(f'Sorted list: {array}')


my_array = [15, 9, 27, 13, 65]
bubble_sort(my_array)



# двоичный поиск по блок-схеме

N=5000
ResultOk=False
First=0
Last=N-1
A=range(5000)
Val=A[357]
Pos=Val

while First<Last:
    Middle=(First+Last)//2
    if Val==A[Middle]:
        First=Middle
        Last=First
        ResultOk=True
        Pos=Middle
    elif Val>A[Middle]:
        First=Middle+1
    else:
        Last=Middle-1

if ResultOk==True:
    print(f'Элемент найден')
    print(Pos)
else:
    print('Элемент не найден')


















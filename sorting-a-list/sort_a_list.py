def selection_sort(L):
    for i in range(len(L) - 1):
        smallest = i
        for j in range(i + 1, len(L)):
            if L[j] < L[smallest]:
                smallest = j
        L[i], L[smallest] = L[smallest], L[i]


L = input("Enter the list of numbers: ").split()
L = [int(x) for x in L]
selection_sort(L)
print("Sorted list: ", end="")
print(L)
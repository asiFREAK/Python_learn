# Find the maximum product of three elements in a list.

def max_product(l):
    maxi = 0
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] * l[j] * l[k] > maxi:
                    maxi = l[i] * l[j] * l[k]
    return maxi
    

list = [1,3,5,7,9,8,6,4,2]
print(max_product(list))
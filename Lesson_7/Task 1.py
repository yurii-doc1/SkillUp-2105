a = [1, 3, 5, 7, 8]

# произведение элементов списка целых
def numbers(a):
    c = 1
    for i in a:
        if i != 0:
            c += i    
    return c
    
print("произведение элементов:", numbers(a))

#нахождения минимума в списке целых

def minimum(a):
    return(min(a))
    
print("минимум в списке:", minimum(a))

# количество простых чисел в списке целых

def num(a):
        count = 0      
        for i in a:
            if i != 0:
                count += 1
        return count 

print("количество простых чисел в списке:", num(a))
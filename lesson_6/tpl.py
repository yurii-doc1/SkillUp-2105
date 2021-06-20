a = (1, 5, 7, 9)
b = (5, 6, 7, 8)
c = (2, 5, 3, 10)
d = tuple(set(a) & set(b) & set(c)) #Elementi kotorie est u vsech tuple
print(d)

# unikalnie elementy dla kazhdeho spiska
f_a = tuple(set(a) - set(b) - set(c))
f_b = tuple(set(b) - set(a) - set(c))
f_c = tuple(set(c) - set(b) - set(a))
print(f_a, f_b, f_c)

# Elementy kototri est v kazhdom kortezhe i nahodatsia na v kazdom kortezhe na toi zhe pozicie

print(a[:-1])
print(b[:-1])
print(c[:-1])
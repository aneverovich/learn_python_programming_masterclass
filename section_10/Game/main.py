a = 3
b = "tim"
c = 1, 2, 3

# int.__str__()
print(a)
# str.__str__() ???
print(b)
# tuple.__str__()
print(c)

# inhertance from object.__str__()

x = object()

for line in dir(x):
    print(line)

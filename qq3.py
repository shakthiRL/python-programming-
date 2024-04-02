def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "not"
    return a / b
radd = add(5, 3)
rsub = sub(5, 3)
rmult = mult(5, 3)
rdiv = div(5, 3)
print("add", radd)
print("sub", rsub)
print("mult", rmult)
print("div", rdiv)

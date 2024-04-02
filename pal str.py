def ispal(n):
    return n==n[::-1]
n="sha"
pal=ispal(n)
if pal:
    print("yes")
else:
    print("no")

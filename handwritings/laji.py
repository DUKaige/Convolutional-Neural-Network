__author__ = 'liukaige'
def reverseString(s):
    a = ""
    b = len(s)
    for i in range(0,b):
        a += s[b - i - 1]
    return a

print reverseString("9283471932847")
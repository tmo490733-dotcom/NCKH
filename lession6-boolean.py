print(10>5)
print(bool(""))
print(bool(None))
print(bool(()))
print(bool("strings"))
print(bool(15))
print(bool(0))

class myfriend():
    def __len__(self):
        return 0
print(bool(myfriend()))

def myFunction():
    return False
if myFunction():
    print("YES!")
else:
    print("NO!")

x=2000
print(isinstance(x,int))
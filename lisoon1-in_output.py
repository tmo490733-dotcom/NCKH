print("hello world")
print("phep toan dau tien : 3 * 3 =",end=" ")
print(3*3)
print("ket qua ", 9 ,"la ket qua cua phep toan dau tiên")
#this is a comment

# biến

x=5
X="Jonhn"
print(x,X)
x=str(5)
_x=9
print(x+X)
print(type(x),"  ",type(_x))
x,y,z="banana","cherry","orange"
print(z)
fruits = ["apple","phone-number","accoutant"]
x,y,z=fruits                            #biến toàn cục 
print(x+y,z)
def myfunc():
    global a                            #biến toàn cục
    a = "stiker"                        
    x = " tem"                           #biến cục bộ
    print(a+x)
myfunc()
print(a+x)
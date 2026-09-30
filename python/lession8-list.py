mylist=["apple","cherry","banana","cherry"]     #cho phép trùng lặp
print(mylist)
print(len(mylist))
list1=[0,"banana",True,False]
print(type(list1))

#hàm tạo
thislist = list(("apple","banana","cherry"))
print(thislist)

#truy cập
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#ktra
if "apple" in thislist:
    print("yes , 'apple' is in the fruits list")
else:
    print("No , 'apple' is in the fruits list")

#thay đổi
thislist[1:2]=["blackcurrant","wertermelon"]
print(thislist)

#thêm mục vào danh sách 
thislist.append("orange")
thislist.insert(2,"kiwi")   
print(thislist)
thislist=['banana','charry']
tropical=["mango","cherry"]
thislist.extend(tropical)
print(thislist)

#xóa các mục trong danh sách (remove list items)
thislist=["apple","banana","charry","banana"]
thislist.remove("banana") 
print(thislist)
thislist.pop(len(thislist)-1)
print(thislist)
thislist=[0,"apple",1,"mechin",2,"cherry",3,"computer"]
del thislist[0:3]
print(thislist)
del thislist    #xóa list
thislist=["apple","banana","charry","banana"]
thislist.clear()
print(thislist)     #xóa sạch list

#vòng lặp (loop)
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(x)
print("\n")
for i in range (len(thislist)):
    print(thislist[i])
print("\n")
i = 0
while i < len(thislist):
    print(thislist[i])
    i+=1
print("\n")
[print(x) for x in thislist]
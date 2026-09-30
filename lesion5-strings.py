a="""xin chao moi nguoi 
minh ten la mo
la mot nguoi moi bat dau hoc python"""
print(a)

print(a[:18])
print(a[-11:-5])

for x in "ban" :
    print(x)

print(len(a),"\n",len(x))

print("\n từ khai niem có trong chuỗi a","khai niem" in a ,"\n từ a có trong chuỗi x","a" in x)
print(x[0])
if "mo" in a:
    print("từ mơ có trong chuỗi a.")
print("mo" not in a)

b="hello, world"
print(b.upper())                #in hoa
print(b.lower())                #thường
print(b.strip())                #bỏ khoảng trăng
print(b.replace("H","J"))       #thay thể H = J
print(b.split(","))             #tách chuỗi thành list

#age=36 ; txt="string" -> thông thể cộng : age+txt -> dùng f
age=10
name="Tran Thi Mo"
print(f"my name is {name}, I'm {age + 9:.2f}")

#Ký tự thoát là một dấu gạch chéo ngược \theo sau là ký tự bạn muốn chèn.
        #xem lại bài thoát khỏi các nhân vật
#xem lại bài phương thức chuỗi
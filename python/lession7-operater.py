print("10 và 5")
print("+ = ",10+5,"\t- = ",10-5,"\t* = ",10*5)
print("/ = ",10/5,"\t% = ",10%5,"\t** = ",10**5,"\t// = ",10 // 5)
"""/ : phép chia trả về float
// : phép chia trả về int
** : số mũ
"""

# gán
x=5
print("\n",x)
x+=3                #- * ... cũng tương tự
print(x)
x=5
x&=3                   # work with bit : end-> or-> xor : còn dịch bit và đảo bit
print(x)
x=5
x|=3
print(x)
x=5
x^=3
print(x)
x=5
print(x:=3)          #operator hải mã : gán giá trị cho các biến như 1 phần bthuc > hơn

number=[1,2,3,4,5]
if (count := len(number)) > 3:
    print(f"list has {count} elements")

#operator 3 ngôi : là bthuc điều kiện
num =6
x="WEEKEND!" if num>6 else "Workday"
print("\n",x)
num=2
x="zero" if num==0 else "one" if num==1 else "two" if num==2 else "three" if num==3 else "don't find number"
print(x)

#so sánh : == ; != ; > ; < ; >= ; <= : kq trả về False or True
x=5
print("\n",1<x<10)  # 1<x<10 = 1<x and x<10 :

#operator logic : sd kết hợp vs đk gồm có and(và) , or(hoặc) , not : vd not(x<5 and x>1

#operator nhận dạng
x=["aple","banana"]
y=x
print("\n",x is y)       #x và y có cùng tham chiếu đến 1 object (ô nhớ) k
print(x is not y)

#operator thành viên : gồm in và not in

#operater bit 

# thứ tự ưu tiên of operater : và kênh w3school xem trong phần operater -> thứ tự ưu tiên

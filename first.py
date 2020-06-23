a=10
b=3
print("a:",a)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print('나눗셈의 몫',a//b)
print(type(a//b))

a="hello"
b='good'
print(a)
print(b)
# a==hello
print(a*100)
print(a[1])
print(a[1:3])
print(a[:3])
print(a.replace('l','b'))
print(a)
#mytxt=int(input("여기에다 입력하세요 : "))
#print(type(mytxt))
mylist = list()
mylist2 = []
mylist3 = [1,2,3,4]
mylist4 = ['글자',1,['숫자',5]]
print(mylist4)
#편리한 기능
mylist.append("1")
mylist.append("2")
mylist.append("4")
mylist.append("3")
print(mylist)
mylist.remove("2")
print(mylist)
mylist.pop()
mylist.reverse()
print("반전",mylist)
mylist.sort()
print("오름차순",mylist)
tmp_str = "+".join(mylist)
print(tmp_str)

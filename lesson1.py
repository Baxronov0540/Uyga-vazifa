# #1
# s1="Mening ismim Eshmat emas"
# prin#t(s1)
# #2
# my_info="""Asror
# Baxronov
# 19
# Navoiy viloyati"""
# prin#t(my_info)
# prin#t(my_info[23])
# #4
# s1="O'zbekiston kelajagi buyuk davlat"
# print#(len(s1))
# #5
# if "buyuk" in s1:
#     print#("Bor")
# else:
#     print#("Yuq") 
# #6
# if "O'zbekiston" in s1:
#     prin#t("O'zbekiston")
# else:
#     pri#nt("bunday so'z yuq")
# #7
# s2=s1.#find("davlat")
# s3=s13[0:s2]
# print3(s3) 
# #8
# s5=s1.#find("buyuk")
# s7=s1#[s5+len("buyuk")::]
# print#(s7)        
# #9
# A=10 >9
# b=11<9
# c=10==10
# print#(A,b,c)
# #10
# a="Eshmat"
# b=10
# print(bool#(a),bool(b))
# #11
# v=10%3
# q=21/4
# w=37//6
# f=7**2
# print(v,q,w,f)
# #12
# x=10
# a= x<5 and x<10
# b=x<5 or x<4
# c=not x==10
# print(a,b,c)
# #13
a= int(input("Balnin kiriting: "))

if 90<=a<=100:
    print("A")
elif 70<=a<90:

    print("B")
elif 60<=a<70:
    print("C")
elif 50<=a<60:
    print("D") 
elif 40<=a<50:
    print("E")
else:
    print("F")    
# #14
x=int(input("sonni kiriting: "))
# if x>10:
#     print("Eshmat")
print("Eshmat") if x>10 else print("Toshmat")
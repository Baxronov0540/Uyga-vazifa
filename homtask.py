#8
# k=int(input("o'ylagan sonni kirting: "))
# while True:
#     n=int(input("siz o'ylagan sonni kiriting; "))
#     if n==k:
#         print("javob to'g'ri: ",k)
#         break
#     elif n>k:
#         print("Kichik")
#         continue
#     else:
#         print("Katta")
#         continue
# #9
# k=int(input("sonni kirting: "))
# a=int(input("sonni kirting; "))
# while True:
#     l=input("amalni kiriting: ")
#     if "q"==l:
#         print("dastur yakuniga etdi!")
#         break
#     elif  "+"==l:
#         print(a+k)
#     elif "-"==l:
#         print(a-k)
#     elif "*"==l:
#         print(a*k)
#     elif "/"==l:
#         print(a/k)
#10
# i=0
# parol=input("parol= ")
# while True:
#    k=input("parolni kiriting; ")
#    if k==parol:
#       print("Muvafaqiyatli!")
#       break
  
#    elif i==3:
#       break
#    i+=1
#########2-bob
# #2
# # i=0
# # s=0
# # while i<5:
# #     k=int(input("sonnim kiritng; "))
# #     s+=k
# #     i+=1
# # print(s)    
# #3
# l=int(input("sonni kiritng; "))
# s=0
# i=0
# k=len(str(l))-1
# while i<=k:
#     s+=int(str(l)[i])
#     i+=1
# print(s)
#7
# l=int(input("sonni kiritng; "))
# k=int(input("sonni kiritng; "))
# i=1
# max_=1
# if l>k:
#  while i<=k:
#   if l%i==0 and k%i==0:
#    max_=i
#   i+=1
#  print(max_)  
# else:
#  while i<=l:
#   if l%i==0 and k%i==0:
#    max_i=i
#   i+=1   
#  print(max_)
#8
# i1=1
# i2=1
# s=2
# k=0
# print(1)
# print(1)
# while s<=10:
#   k+=i2+i1
#   s+=1
#   print(k)
#   i1=i2
#   i2=k
#   k=0
#9
# while True:
#     a=int(input("a= "))
#     b=int(input("b= "))
#     c=int(input("c= "))
#     if a+b>c and a+c>b and c+b>a:
#         print("Uchburchak yasaldi uning perimetri:",a+b+c)
#         break
#     else:
#         continue    
# k=int(input("balansni kiritng; "))
# while k>=0:
#   p=input("pul qo'ymoqchi bolsangiz (1 ni kirting:) yoki  pul yechmoqchi bo'lsangiz (0 ni kiriting: )")

#   if p==1:
#     l=int(input("pul miqdorini kiriting; "))
#     k+=l
#   elif p==0:
#     l=int(input("yechmoqchi bo'lgan pul miqdorini kirting; "))
#     k-=l
##########3 b0b
#2
# k= input("so'zni kiritng: ")
# i=0
# m=0
# p=len(k)-1
# l="bcdfghjklmnpqrstxwzvy" 
# while i<=p:
#     if k[i] in l:
#      m+=1
#     i+=1
# print(m)          
#5
# k=input("matnni kirting ;")
# i=0
# n=len(k)-1
# s=""
# while i<=n:
#     if k[i]!=" ":
#         s+=k[i]
     
#     i+=1
# print(s)    
# #5
# l=input("so'zni kiriting; ")
# q="aeiuo"
# i=0
# w=len(l)-1
# while i<=w:
#     if l[i] in q:
#         print(i)
#         break
#     i+=1 
# #8
# s=input("matnni kiritng; ")
# max_len=int(input("matnni uzunligini kiriting; ") )
# i=0
# m=""
# p=""
# while i<=len(s)-1:
#   if max_len>=i:
#    p+=s[i]


#   i+=1
# print(p)  
##9
# l=input("shifirlanishi kutiladigan matnni kiriting ; ")
# i=0
# k=len(l)-1
# s="abcdefghijklmnopqrstuvxyzwABCDEFGHIJKLMNOPQRSTUVXWZY"
# t=""
# while i<=k:
#     if l[i] in s:
#         if "z"!=l[i] or "Z"!=l[i]:
#          m=ord(l[i])
#          t+=chr(m+1)
#         elif "z"==l[i]:
#            t+="a"
#         elif "Z"==l[i]:
#               t+="A" 
#     else:
#         t+=l[i]
#     i+=1 
# print(t)       
#####4-bob
#1
# k=int(input("tub sonni kiritign ;"))
# i=2
# topildi=False
# while i<=(k)**0.5:
#     if k%i==0:
#         print("tub emas!")
#         topildi=True
#         break
        
#     i+=1     
# if not(topildi):
#     print("Tub son")
#2
# k=int(input("Maxfiy sonni kiriting; "))
# i=0
# while i<5:
#     n=int(input("sonni kiriting: "))
    
#     if n==k:
#         print("siz yutdingiz!")
#         break
#     i+=1
    
#3
# import time
# n= int(input("sonni kirting; "))

# while True:
#     if n%2==0:
#         n=n/2
#         print(n)
#     else:
#         n=n*3+1
#         print(n)
#     if n==1:
#         break
#     time.sleep(1)        
##4
# import random
# l=random.randint(1,100)
# while True:
    
#     n=int(input("sonni kiriting; "))
#     if n==l:
#      print("siz topdingiz")
#      break
#     elif n>l:
#        print("Katta")
#     else:
#        print("kichik")       
##5

# s=int(input("summani kiritng; "))
# f=int(input("foizni kiriting: %"))
# l=int(input("oylik to'lovni kiriting; "))
# i=0
# m=l
# while s>0:
#     k=s*(f/100)/12
#     l-=k
#     if s<l:
#         l=s

#     s-=l
#     i+=1
#     l=m
# print(i,s)    
# #7
# s=0
# while True:
#     k=int(input("sonni kiriting; "))
#     if k<0:
#         print(s)
#         break
#     s+=k
# #8
# s=int(input("tashlanadigan pul miqdori: "))
# while True:
#     m=int(input("mahsulot narxi : "))
#     if s>=m:
#         s-=m

#     if m==0:
#         break 
##9
# while True:
#     print("\n=== Oddiy Kalkulyator Menyusi ===")
#     print("1. Qo'shish")
#     print("2. Ayirish")
#     print("3. Chiqish")

#     tanlov = input("Tanlovingizni kiriting (1/2/3): ")

#     if tanlov == "1":
#         a = float(input("1-sonni kiriting: "))
#         b = float(input("2-sonni kiriting: "))
#         print("Natija:", a + b)

#     elif tanlov == "2":
#         a = float(input("1-sonni kiriting: "))
#         b = float(input("2-sonni kiriting: "))
#         print("Natija:", a - b)

#     elif tanlov == "3":
#         print("Dastur tugadi. Xayr!")
#         break   # sikldan chiqish

#     else:
#         print(" Noto‘g‘ri tanlov! Qayta urinib ko‘ring.")


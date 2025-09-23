##########shart operatorlari
#1
# a=int(input("sonni kiritng: "))
# if a>0:
#     print(a+1)
# else:
#     print(a)
#2
# a= int(input("sonni kirting: "))
# if a>0:
#     print(a+1)
# else:
#     print(a-2)    
#3
# a= int(input("sonni kirting: "))
# if a>0:
#     print(a+1)
# elif a==0:
#     print(10)
# else:
#     print(a-2)     
# #4
# a= int(input("sonni kirting: "))
# b= int(input("sonni kirting: "))
# c= int(input("sonni kirting: "))
# if a>0:
#     if b>0:
#         if c>0:
#             print(3)
#         else:
#             print(2)    
#     else:
#         if c>0:
#             print(2)
#         else:
#             print(1)
# elif a<0:

#     if b>0:
#         if c>0:
#             print(2)
#         else:
#             print(1)    
#     else:
#         if c>0:
#             print(1)
#         else:
#             print(0)
# #5
# a=int(input("sonni kirting: "))                    
# b=int(input("sonni kirting: "))
# c=int(input("sonni kirting: "))
# if a>0:
#     if b>0:
#         if c>0:
#             print("musbat sonlar:",3,"manfiy sonlar: ",0)
#         else:
#             print("musbat sonlar:",2,"manfiy sonlar: ",1)    
#     else:
#         if c>0:
#             print("musbat sonlar:",2,"manfiy sonlar: ",1)
#         else:
#             print("musbat sonlar:",1,"manfiy sonlar: ",2)
# elif a<0:

#     if b>0:
#         if c>0:
#             print("musbat sonlar:",2,"manfiy sonlar: ",1)
#         else:
#             print("musbat sonlar:",1,"manfiy sonlar: ",2)    
#     else:
#         if c>0:
#             print("musbat sonlar:",1,"manfiy sonlar: ",2)
#         else:
#             print("musbat sonlar:",0,"manfiy sonlar: ",3)
#6
# c=int(input("sonni kirting: "))
# a=int(input("sonni kirting: "))
# if (a>c):
#     print(f"{a} katta {c}dan")
# elif a==c:
#     print("ikkalasi ham teng!")
# else:
#     print(f"{c} soni {a} dan katta") 
# #7
# a=int(input("sonlarni kiriting: "))
# b=int(input("sonlarni kiriting: "))
# if a>b:
#     print(b)
# elif a==b:
#     print(a,b)
# else:
#     print(a)       
#8
# a=int(input("sonlarni kiriting: "))
# b=int(input("sonlarni kiriting: "))
# if a>b:
#     print(a,b)
# elif a==b:
#     print(a,b)
# else:
#     print(b,a)
#9
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting; "))
# if a>b:
#     a,b=b,a
#     print("A:",a,"B:",b)
# elif b>a:
#     print("A:",a,"B:",b)    
#10
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# if a==b:
#     a=0
#     b=0
#     print(a,b)
# else:
#     a,b=a+b,a+b
#     print(a,b)
# #11
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# if a==b:
#     a,b=0,0
#     print(a,b)
# else:
#     if a>b:
#         a,b=a,a
#         print(a,b)
#     else:
#         a,b=b,b 
#         print(a,b)       
#12
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kirting; "))
# if a>b and a>c:
#     if b>c:
#         print(c)
#     else:
#         print(b) 
# elif b>a and b>c:
#     if a>c:
#         print(c)
#     else:
#         print(a)
# else:
#     if a>b:
#         print(b)
#     else:
#         print(a)                         
#13
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kirting; "))
# if a>b and a>c:
#     if b>c:
#         print(b)
#     else:
#         print(c) 
# elif b>a and b>c:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if a>b:
#         print(a)
#     else:
#         print(b)                         
#14
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kirting; "))
# if a>b and a>c:
#     if b>c:
#         print(a,c)
#     else:
#         print(a,b) 
# elif b>a and b>c:
#     if a>c:
#         print(b,c)
#     else:
#         print(b,a)
# else:
#     if a>b:
#         print(c,b)
#     else:
#         print(c,a)
#15
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kirting; "))
# if a>b and a>c:
#     if b>c:
#         print(a+b,a+c)
#     else:
#         print(a+c,b+a) 
# elif b>a and b>c:
#     if a>c:
#         print(b+a,c+b)
#     else:
#         print(b+c,a+b)
# else:
#     if a>b:
#         print(c+a,b+c)
#     else:
#         print(c+b,a+c)

#16
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kiriting: "))
# if a<=b<=c:
#     print(2*a,2*b,2*c)
# else:
#     print(-a,-b,-c)

#17
# a=int(input("sonni kiriting: "))
# b=int(input("sonni kiriting: "))
# c=int(input("sonni kiriting: "))
# if a<=b<=c or a>=b>=c:
#     print(2*a,2*b,2*c)
# else:
#     print(-a,-b,-c)
#18
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))

# if a <= b and a <= c:
#     t= 1
# elif b <= a and b <= c:
#     t = 2
# else:
#     t = 3

# print(t)
#19
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
# d= int(input("4-sonni kirting: "))
# if a==b==c>d:
#     print(4)
# elif a==b==d>c:
#     print(3)
# elif a==c==d>b:
#     print(2) 
# elif c==b==d>a:
#     print(1)
# else:
#     print("shartga mutanosib emAS!")
#20
import math
# xa=int(input("kordinatani kiriting: "))
# ya=int(input("kordinatani kiriting: "))
# A=(xa,ya)
# xb=int(input("kordinatani kiriting: "))
# yb=int(input("kordinatani kiriting: "))
# B=(xb,yb)
# xc=int(input("kordinatani kiriting: "))
# yc=int(input("kordinatani kiriting: "))
# C=(xc,yc)
# if math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)>math.sqrt((A[0]-C[0])**2+(A[1]-C[1])**2):
#     print("c",math.sqrt((A[0]-C[0])**2+(A[1]-C[1])**2))
# else:
#     print("B",math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2))
#21
# xa=int(input("kordinatani kiriting: "))
# ya=int(input("kordinatani kiriting: "))
# A=(xa,ya)
# if A[0]==0 and A[1]==0:
#     print(0)
# elif A[1]==0:
#     print(1)
# elif A[0]==0:
#     print(2)
# else:
#     print(3)            
#22
# xa=int(input("kordinatani kiriting: "))
# ya=int(input("kordinatani kiriting: "))
# A=(xa,ya)
# if A[0]>0 and A[1]>0:
#     print("I chorak")
# elif A[1]>0 and A[0]<0:
#     print("II chorak")
# elif A[1]<0 and A[0]<0:
#     print("III chorak")      
# else:
#     print("IV chorak")

# #23
# x1=int(input("x1 sonni kiriting:"))
# y1=int(input("y1 sonni kiriting:"))
# x2=int(input("x2 sonni kiriting:"))
# y2=int(input("y2 sonni kiriting:"))
# x3=int(input("x3 sonni kiriting:"))
# y3=int(input("y3 sonni kiriting:"))
# if x1==x2:
#   x4=x3
# elif x1==x3:
#   x4=x2 
# elif x3==x2:
#   x4=x1   
# if y1==y2:
#   y4=y3
# elif y3==y1:
#   y4=y2
# elif y3==y2:
#   y4=y1
# print(x4,y4)
#24
#x= float(input("x haqiqiy sonlar berilgan: "))
# if x>0:
#     print(2*math.sin(x)) 
# else:
#     print(x-6)
#25
# x= float(input("x haqiqiy sonlar berilgan: "))
# if x<-2 or x>2:
#     print(2*x)
# else:
#     print(-3*x)
#26
# x= float(input("x haqiqiy sonlar berilgan: "))
# if x<=0:
#     print(-x)
# elif 0<x<2:
#     print(x**2)
# elif x>=2:
#     print(4)
#27
# x= float(input("x haqiqiy sonlar berilgan: "))
# if x<0:
#     print(0)
# elif x%2==0:
#     print(1)
# elif x%2==1:
#     print(-1)
#28
# yil=int(input("yilni kiriting: "))
# if yil%100==0 and yil%400==0:
#     print(366)
# elif  yil%100!=0 and yil%4==0:
#     print(366)
# else:
#     print(365)         
#29
# x= int(input("sonni kiriting: "))
# if x>0 and x%2!=0:
#     print("musbat toq son!")
# elif x<0 and x%2==0:
#     print("Manfiy juft son!")
# elif x==0:
#     print("son nolga teng!")
#30
# x= int(input("1-999 sonini oraliqdagi sonni kiriting: "))
# if 10<=x<=99 and x%2==0:
#     print("ikki xonali juft son !")
# elif 100<=x<=999 and x%2==0:
#     print("uch xonali juft son!")   
####shoh yurishi
# x1=int(input("x1= "))
# y1=int(input("y1= "))
# x2=int(input("x2= "))
# y2=int(input("y2= "))
# q= ((x1==x2 or y1==y2) and (abs(y2-y1)<=1 and abs(x1-x2)<=1) ) or (abs(x1-x2)==abs(y1-y2)==1)
# print(q)
########## ot yorishi
# # 
# x1=int(input("x1= "))
# y1=int(input("y1= "))
# x2=int(input("x2= "))
# y2=int(input("y2= "))
# q= (abs(x2-x1)==2 and abs(y2-y1)==1) or (abs(x2-x1)==1 and abs(y2-y1)==2)
# print(q)

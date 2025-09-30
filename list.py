
#1
# k=list("olma","o'rik","nok,","behi","olcha")
# print(k)
#2
# k=[]
# for i in range(1,11):
#     k.append(i)
# print(k)    
# #3
# my_shoppingAA_CAR=list()
# print(my_shoppingAA_CAR)
# l=[1,2,3,4,5]
# print(l[2])

# #5
# l=[1,2,3,4]
# print(l[-1])
#6
# l=[1,2,3,4,5]
# print(l[0:3])
#7
# l=[1,2,3,4,5,6,7,8,9,0]
# k=l[3:8]
# print(k)
#8
# k=list("olma","o'rik","nok,","behi","olcha")
# if "olma" in k:
#     print("BU meva bor")
# else:
#     print("bu meva yuq")    
#################2222222#####################
# k=list("olma","o'rik","nok,","behi","olcha")
# k.append("uzum")
# print(k)
#2
# k=list("olma","o'rik","nok,","behi","olcha")
# k.insert(1,"mongo")
# print(k)
#3
# k=["olma","o'rik","nok,","behi","olcha"]
# k[0]="kivi"
# print(k)

#4
# k=["olma","o'rik","nok,","behi","olcha"]
# k.pop()
# print(k)
#5
# k=list("olma","o'rik","nok,","behi","olcha")
# k.remove("olma")
# print(k)

#6
# k=["olma","o'rik","nok,","behi","olcha"]
# k.clear()
# print(k)
#7
# k=["Asror","Arif","Bexruz","Shahboz"]
# l=[18,22,19,19]
# k.extend(l)
# print(k)

#8
# l=[18,22,19,19]
# l1=l.copy()
# l[0]=12
# print(l1,l)

################333333################
# k=["olma","o'rik","nok,","behi","olcha"]
# for i in k:
#     print(i)
#2
# l=[1,2,3,4,5,6,6,7]
# i=0
# k=0
# while True:
#     if l[i]<=5:
#         print(l[i])
#     i+=1    
#     if len(l)==i:
#         break
#3
# k=["olma","o'rik","nok,","behi","olcha"]
# for i in k:
#     if "a" in i:
#         print(i)
#45
# l=[1,2,4,4,567,6,87,9,79,9,10]
# for i in l:
#     if i%2==0:
#         print(i)
#5
# l=[1,2,4,4,567,6,87,9,79,9,10]
# s=0
# for i in l:
#     s+=i
# print(s)
#6
# import random
# l=[]
# for i in range(10):
    
#     l.append(random.randint(1,1000))
# print(l)
# k=l[0]
# for i in l:
#     if k<=i:
#         k=i
# print(k)        
#7
# l=["banan","olam","bexruz","banan"]
# k=l.count("banan")
# print(k)
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(l)):
#     l[i]=l[i]**2
# print(l)    
# l=["Asror","Bexruz","wer","olim"]
# for i in l:
#     if len(i) >=5:
#         print(i)
#3
# l=["Asror bugun maktabga keldi","Bexruz ertalab kech turdi","Shahboz kecha darsga  "]
# for i in range(len(l)):
#     l[i]=l[i].upper()
# print(l)    
##################################4################
# l=["Asror bugun maktabga keldi","Bexruz ertalab kech turdi","Shahboz kecha darsga  "]
# for i in l:
#     print(i,len(l))
#2
# l=list(1,2,True,"Bexruz frontenchi")
# print(l)
#3
# l=["Asror bugun maktabga keldi","Bexruz ertalab kech turdi","Shahboz kecha darsga  "]
# print(l[::-1])
    
#5
# l=[12,23,34,345,4]
# l1=[4,34,65,62,312312,4,1,3,325,32]
# l3=[]
# for i in l:
#     if i in l1:
#         (l3.append(i))

# print(l3)
#6
# kl=[1,24,41,2,11223,2,1132,211,1]
# for j,i in enumerate(kl):
#     if kl.count(i)>1:
#         kl.pop(j)
# print(kl)        
#6

# l=["Asror bugun maktabga keldi","Bexruz ertalab kech turdi","Shahboz kecha darsga  "]
# print(sorted(l))

#7
# l=[1,2,34,4,56,7,8,0,9]
# l.sort
# l.reverse()
# print(l)

#8
# l=["Asror","Bexruz","Shahboz"]
# for i in range(len(l)):
#     l[i]=f"Salom ,{l[i]}"
# print(l)    

#9
# l=[]      
# for i in range(5):
#     a=input("isimni kirting; ")
#     l.append(a)
# print(l)    
#10
# n= int(input("a = "))
# l=[]
# for i in range(n):
#     l.append(0)
# print(l)
# #11
# l="Asror men bugun ishlarim zor"
# k=l.split()
# print(k)
#12
# l=["asror","bexruz","shahboz"]
# k="".join(l)
# print(k)
#13
# l=[2,3,4,5,4,3,4,4,5,3]
# k=0
# j=0
# for i in l:
#     k+=i
#     j+=1
# print(k/j)    
#14
# l=[]
# while True:
#     n=input("sonni kiritng; ")
#     if n=="done":
#         break
#     l.append(float(n))
# print(l)
########tuple############
#1
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# print(t)
#2
# y=("Python",)
# print(type(y))
#3
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# print(t[0])

#4
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# print(t[len(t)-3:len(t)])
#5
# ranglar=("qizil","Yashil","Ko'k")
# r1,r2,r3=ranglar
# print(r1,r2,r3 ,end="/n")
#6
# t= ("qizil", "yashil", "ko‘k",)
# t[1]="oq"
# print(t[1]) 
#7
# t=("Monday","Tuesday","Wednesday",)
# if "Tuesday" in t:
#     print("Bor")
#8
# m=("a","b","c","a",)
# m.count("a")
# print(m)
#9
# l=("red","blue","green","yellow")
# k=l.index("red")
# print(k)
####################2###############################
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# l=list(t)
# print(l)
#2
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# l=list(t)
# l.append("Funday")
# print(tuple(l))

#3
# matn="hello"
# t=tuple(matn)
# print(t)
# #4
# l=(1,2,)
# l1=(3,4,)
# l=l1+l
# print(l)
#5
# m=(1,2,3,)
# print(3*m)
#6
##########################3####################
# l=(1,2,3,4,5,6,)
# for i in l:
#     print(i)
#2
# l=("h","e","l","l","o")
# i=0
# while i<=len(l)-1:
#     print(l[i])
#     i+=1
#3
# l=(1,2,4,5,7,3,5,5,)
# for i in l:
#     if i%2!=0:
#         print(i)
#4
# l=(1,2,4,5,7,3,5,5,)
# s=0
# for i in l:
#     s+=i
# print(s)
#5
# t=("Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba",)
# for i in t:
#     print(len(i)
#           )
#6
# t=((1,2),(3,4),)
# for i in t:
#     print(i)
####################4##########################
#1
# def Max():
#     kl=[1,3,1,3,4,5,778,23,11,90]
#     max=kl[0]
#     for i in kl:
#         if max<=i:
#             max=i
#     min=kl[0]
#     for j in kl:
#             if min>=j :
#                    min=j
#     return print((min,max,))
# Max()                
#2
# for i in range(4):
#     x1=int(input("x= "))
#     y1=int(input("y= "))
#     m=(x1,y1,)
#     print(m)
#3
# kalit=("ism","yosh","manzil")
# dict={kalit:"bu kortejga tegishli"}
# print(dict)

#4
# l=["ism","yosh","manzil"]
# dict={l:"ewrewr"}
# print(dict)
#5
# l=[]
# for i in range(3):
#     y=input("isimni kiriting; ")
#     a=int(input("yoshni kiriting; "))
#     t=(y,a)
#     l.append(t)
# print(l)    

#6
# l=[]
# for i in range(3):
#     y=input("isimni kiriting; ")
#     a=int(input("yoshni kiriting; "))
#     t=(y,a)
#     l.append(t)
# print(l)    
# for j in l:
#     print(j)
#7
# l=[]
# for i in range(3):
#     y=input("isimni kiriting; ")
#     a=int(input("bahosini kiriting; "))
#     t=(y,a)
#     l.append(t)
# for j in (l):
#         list(j)[1],list(j)[0]=list(j)[0],list(j)[1]

# l.sort()
# for k in l:
#   list(k)[0],list(k)[1]=list(k)[1],list(k)[0]
# print(l)  


# #8
# l=[1,-4,23,-3,324,-45,242,-56,-78,90]
# m=list()
# n=list()
# for  i in l:
#     if i>0:
#         m.append(i)
#     else:
#         n.append(i)
# print(tuple(m),tuple(n))            
#9
# l="Hello World"
# k="aeiou"
# l1=[]
# for i in l:
#     if i in k:
#       l1.append(i)
# print(tuple(l1))            
#10
# l=[]
# for i in range(4):
#     y=input( "foydalnuvchi nomi: ")
#     e=input("email: ")
#     j=input("sana: ")
#     m=(y,e,j)
#     l.append(m)
# print(tuple(l))    
# #11
# l=(1,2,3,4,5,6,-4,24)
# k=0
# for i in l:
#     if i>0:
#       k+=1
# if len(l)==k:
#    print("Kortejdagi hamma sonlar musbat!")
# else:
#    print("Kortejdagi sonlarni hammsai musbat emas!" )              
#12
# l=(1,2,3,4,5,5,5,6,)
# for i ,j in enumerate(l):
#     print(i,j)
#13
# l=("olma","nok","olcha","uzum","apelsin")
# for i in l:
#     print("meva")
#14
# l=("Asror","Bexruz","Shahboz","Arif","Abdulloh","Abror","Axror","MUhammadALI")
# k=l[0]
# for i in l:
#     if len(i)>=len(k):
#         k=i
# print(k)        
#15
# l=((1,2,3),(4,5,6))
# k=[]
# for j in l:
#    k+= list(j)
# print(tuple(k))   
#16
# l=(1,3,0,5,6,6,3,2,9)
# n=int(input("sonni kiritng; "))
# l.index(n)
# print("Bor")
#17
# l=(1,2,3,4,5,6,12,7,9)
# k=sum(l)/len(l)
# print(l,k)

#18
# def FUN(l):
#     return (l[0],l[-1],len(l))
    
# print(FUN("Asror"))

#19
# for i in range(4):
#     ism=input("ismni kiritng: ")
#     email=input("emailni kiritng; ")
#     age=int(input("yoshni kiritng: "))
#     m=(ism,email,age)
#     print(m)
#20
# import sys
# t=(1,2,3)
# m=[1,2,3]
# print(sys.getsizeof(t),sys.getsizeof(m))
################set#######################
# a={"qora","oq","kulrang","Yashil","qizil"}
# print(a)
#2
# l=[1,2,3,4,2,3]
# print(set(l))
#3
# k=set()

#4
# a={"qora","oq","kulrang","Yashil","qizil"}
# a.add("ko'k")
# print(a)

#5
# a={"qora","oq","kulrang","Yashil","qizil"}
# a.remove("oq")
# print(a)
#6
# a={"qora","oq","kulrang","Yashil","qizil"}
# a.pop()
# print(a)
#7
# a={"qora","oq","kulrang","Yashil","qizil"}
# if "qizil" in a:
#     print(f"qizil bor ekan")
# else:
#     print("qizil yuq ekan")    
#8
# a={"qora","oq","kulrang","Yashil","qizil"}
# for i in a:
#     print(i)
##############2######################
# se1={1,2,3}
# se2={2,3,4,5}
# k=se1.union(se2)
# print(k)
#2
# se1={1,2,3}
# se2={2,3,4,5}
# print(se1.intersection(se2))
#3
# se1={1,2,3}
# se2={2,3,4,5}
# print(se1-se2)
#4
# se1={1,2,3}
# se2={2,3,4,5}
# print(se1.symmetric_difference(se2))
#5
# se1={2,3}
# se2={2,3,4,5}
# print(se1.issubset(se2))
#6
# n=input("matnni kiritng; ")
# a=set(n)
# b={"a","e","i","o","u"}
# print(a.intersection(b))
#7
# se1={1,2,3,6}
# se2={1,2,3,4,5,6,7,8,9}
# print(se2.issubset(se1))
#8
# gap = "salom dunyo salom Python dunyo oson"
# ga=(gap.split())
# k=set(ga)
# for i in k:
#     ga.remove(i) 
# k1=set(ga)
# print(k.difference(k1))  
##################################################
# l=[1,2,3,4,5,1,3,2]
# k=set(l)
# for i in k:
#     l.remove(i)
# k1=set(l)
# print(k.difference(k1))
#2
# n=input("satrni kiriting; ")
# l=input("satrni kiriting; ")
# n1=set(n)
# l1=set(l)
# print(n1.intersection(l1))
#3
# id1=[112,700,540]
# id2=[123,700,340]
# print(set(id1).intersection(set(id2)))
#4
# l=[1,3,4,11,8,2,30]
# s=set()
# for i in l:
#   s.add(i)
# print(s)    
#5
# l=input("matnni kiriting; ")
# a="aieou"
# s=""
# for i in l:
#     if i in a:
#         s+=i
# k=list(s)
# s1=set(s)
# for j in s1:
#     k.remove(j)
# p=set(k)
# print(s1.difference(p))
#6
# t=["Asror","Shahboz","Arif","Bexruz","Asror","Arif","NEmat"]
# s=set()
# for i in t:
#     if t.count(i)>1:
#       s.add(i)
# print(s)        
#7
# l=map(int,input("list= ").split())
# k=list(l)
# s=set()
# for i in k:
#     if i%2==0:
#         s.add(i)
# print(s)        
#8
# l=["baxronovasror77@gmail.com","bexruz0623@gmail.com","baxronovasror77@gmail.com","abror0101@gmail.com","bexruz0623@gmail.com","axrorwats@gmail.com"]
# k=set(l)
# for i in (k):
#     if i in l:
#         l.remove(i)
# k1=set(l)
# print(k.difference(k1))
#9
# l=input("matnni kiriitng; ")
# k=list(l.split())
# q=set(k)
# for i in q:
#     if i in k:
#         k.remove(i)
# w=set(k)
# print(q.difference(w))         
#10
# k=set(range(1,11))
# print(k)
# l=map(int,input().split())
# n=list(l)
# j=set(n)
# print(j.symmetric_difference(k))
#11
# l={"Ikki eshik orasi","Hayot go'zal","Muqqadas ruh","Dunyoning ishlari"}
# k=input("janr nomini kiriting; ")
# g=1
# for i in l:
#     if k==i:
#      print("siz so'ragan janr:",i)
#      g=0
# if g==1:
#    l.add(k)     
#    print(f"{k} janri yuq edi endi to'plamimizga qo'shamiz")
#12
# l=[1,2,3,4,5,1,3,2]
# k=set(l)
# for i in k:
#     l.remove(i)
# k1=set(l)
# print(sum(k.difference(k1)))
#13
# s=input("satrni kiriting: ")
# print(set(s))
#14
# l=[1,2,3,4,5]
# l1=[4,5,6,7,8,9]
# k=set(l)
# k1=set(l1)
# print(k.symmetric_difference(k1))
#15
# fs=frozenset({1,2,4,5})
# fs.add(2)
# print(fs)
#16
""""
list o‘zgaruvchan (mutable): ichidagi elementlarni qo‘shish, o‘chirish, almashtirish mumkin.

Shuning uchun uni hash qilib bo‘lmaydi → demak, set ichiga qo‘yib bo‘lmaydi.
"""
#19
# l={1,2,3,4,5,6,7,8,9,9}
# for i in l:
#    if i%2==0:
#       print("juft",i)
#    else:
#       print("toq",i)   
#20
# l="asror bugun dars qildi"
# k="bexruz ertaga dars qildi"
# t=set(l.split())
# t1=set(k.split())
# print(t1.difference(t))
# #21
# a = input("1-chi sonlar ro‘yxatini kiriting (vergul bilan): ")
# b = input("2-chi sonlar ro‘yxatini kiriting (vergul bilan): ")
# set1 = set(map(int, a.split(",")))
# set2 = set(map(int, b.split(",")))
# kesishma = set1 & set2   

# print("Birinchi to‘plam:", set1)
# print("Ikkinchi to‘plam:", set2)
# print("Kesishma:", kesishma)

#22
# l={"Baxronov Bexruz","Baxronov Asror","Mirvosilov Abdulloh","Masharipov Arifbek","Igor Sergiyev"}
# k=input("k= ")
# if k in l:
#     print("Taqiqlagan")
# else:
#     print("Taqiqlanmagan")    
#23
# import random
# l=[]
# n=int(input("n= "))
# for i in range(n):
#     l.append(random.randint(1,1000))
# e=1
# k=int(input("k ="))
# for j in set(l):
#     if i==k:
#         print("bor")
#         i=0
# if i==1:
#     print("yuq")

#24
# l=input("l= ")
# for i in set(l):
#     if l.count(i)==1:
#         print(i)
    
    
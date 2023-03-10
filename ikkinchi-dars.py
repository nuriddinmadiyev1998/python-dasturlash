
# print("What is no name")
# name=input()
# print("Hello",name)
# name="nuriddin"
# surname="madiyev"
# print("Ismi:", name, "Familyasi:", surname)
#
# a="Hello World!\n"
# print(a*4)
# bow harfni kichkina qiberadi.lower
# a="Hello world!"
# print(a.lower())
# hamma harflani katta qbweradi
# a="Hello world!"
# print(a.upper())
# print(a)
# harflani tuwirup qoldiradi .split
# a="Hello world! My name is Nuriddin Madiyev"
# print(a.split("n"))
#
# ism=input("Ismingiz nima?:")
# print("Assalomu alekum,"+ism)
# RUYXAT(LIST)
# mevalar=["olma","urik","shaftoli","olcha"]
# print("Birinchi meva:",mevalar[0])
# print("ikkinchi meva:",mevalar[3])
#
# cars=["bmw","lexsus","toyota","bmw","dsbjkdvnsidhubfn"]
# cars.sort()
# print(cars)
#
# cars=["Ford","mustang","volvo"]
# cars.sort(reverse=True)
# print(cars)
#
# fruits=["olma","nok","uzum"]
# fruits.reverse()
# print(fruits)
#
# thilist=["olma","anor","olcha"]
# last_element=thilist.pop()
# print(thilist)
# print(last_element)
#
# thilist=["olma","anor","olcha","banan"]
# thilist.remove("olcha")
# print(thilist)
#
# a=["olma","banan","uzum"]
# b=["urik","shaftoli","zardoli"]
# c=a+b
# print(c)
# a.extend(b)
# print(a)
#
# cars=["volvo","nexia","audi","damas","rolsroysn","lasetti","jentra","bentley"]
# cars.sort()
# print(cars)
#
# thislist=("olma","anor","banan")
# print(thislist[0])
# print(thislist[1])
# print(thislist[1:3])
#
# cars=["volvo","nexia","audi","damas","lasetti","jentra","bentley"]
# cars.sort(reverse=True)
# print(cars)
#
# mehmonlar=["Odil","Dilshod","Navruz","Nurbek","Akbar","Shamsiddin","Nuriddin"]
# print("sorted() qaytargan ro'yhat:",sorted(mehmonlar))
# print("Asil ro'yhat o'zgarmas qoldi:",mehmonlar)
#
# fruits=["olma","anor","zardoli","uzum","banan","kivi","mandarin"]
# print("Elementlar soni:",len(fruits))
#
# sonlar=list(range(0,15))
# print(sonlar)
#
# juft_sonlar=list(range(0,20,2))
# toq_sonlar=list(range(1,20,2))
# print("Juft sonlar:", juft_sonlar)
# print("Toq sonlar:", toq_sonlar)
#
# toys=("ot","buzoq","tuya","quyon","tovuq")
# print(toys[0])
# print(toys[2])
# print(toys[0:4])
#
# t_yil=int(input("Tug'ilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("Siz:"+str(yosh)+"yoshda ekansiz")

# mehmonlar=["ALI","Aziz","Nemat","Nuriddin","Avazbek"]
# for mehmon in mehmonlar:
#     print
#
# mehmonlar=["Ali","Vali","Nodir","Akbar","Shavkat","Nuriddin"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon},sizni 16 mart kuni yoziladigan dasturxonimzga lutfan taklif etamiz")
#     print("Hurmat bilan Fayzullayevlar xonadoni
#
# sonlar=list(range(1,15))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
#
# zeros=[3]*10
# print(zeros)
#
# zeros=[i**2 for i in range(10)]
# print(zeros)
#
# squares=[]
# for x in range(10):
#     squares.append(x**2)
# print(squares)
#
# squares=[x ** 2 for x in range(10)]
# print(squares)
#
# squares=[x**2 for x in range(10)]
# print(squares)
# cubes=[x**3 for x in range(10,21)]
# print(cubes)
# chars=[]
# for c in range(80,123):
#     chars.append(chr(c))
# print(chars)

# mehmonlar=["Ali","Vali","Xasan","Nodir",]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}")
#     print("Sizni ertalabki nahorgi oshga taklif etamiz.")
#     print("Hurmat bilan Fayzullayevlar xonadoni")

# dustlar=[]
# print("5 ta eng yaqin dustingiz kim?:")
# for n in range(5):
#     dustlar.append(input(f"{n+1}-ismini kiriting:"))
# print(dustlar)
#
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son}ning kvadrati {son**2} ga teng")
#
# List=[]
# for _ in range(3):
#     for x in "a":
#         List.append(x)
# print(List)
#
# List=[x for _ in range (3) for x in "abcdefgichng"]
# print(List)
#
# ves=[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]
# List=[digit for lst in ves for elem in lst for digit in elem]
# print(List)
#
# squares=[x**2 for x in range(10)]
# print(squares)
#
# cubes=[]
# for i in range(10,21):
#     cubes.append(i**3)
#     print(cubes)
#
# cubes=[i**2 for i in range(10,21)]
# print(cubes)
#
# chars=[]
# for c in range (80,123):
#     chars.append(chr(c))
# print(chars)
#
# n=int(input())
# lines=[input() for _ in range(n)]
# print(lines)

# lines=[input() for _ in range(int(input()))]
# print(lines)
# if-else operatori
# a=[]
# for x in range(1,11):
#     if x % 2 == 0:
#         a.append(x)
# print(a)
#
# list=[]
# for x in range(10):
#     if x % 2 == 0:
#         list.append (x**2)
#     else:
#         list.append(x**3)
#         print(list)
# list=[x**2 if x % 2 == 0 else x ** 3 for x in range(10)]
# print(list)

# list=[]
# for x in range(1,5):
#     for y in range(5,0,-1):
#         if x !=y:
#             list.append([x,y])
#             print(list)
#
# list=[[x,y] for x in range(1,5)for y in range(5,1,-1) if x !=y]
# print(list)
# ichma ich joylawgan takrorlaw
# list=[]
# for _ in range(3):
#     for x in "a":
#         list.append(x)
#         print(list)
#
# list=[x for _ in range(3) for x in "abcdefgh"]
# print(list)
#
# yil=int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18:
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelipsiz!")
#
# a=()
# b=tuple()
# c=tuple(("apple", "banana", "cherry"))
# d="apple", "banana", "cherry"
# e=tuple("Hello!")
# print("a=",a)
# print("b=",b)
# print("c=",c)
# print("d=",d)
# print("e=",e)
#
# thistuple=("abc",34,True,40.12,"male")
# print(thistuple)
#
# thistuple=("olma","anor","banan")
# for x in thistuple:
#     print(x)
#
# x=("olma","anor","uzum")
# print(x)
#
# y=list(x)
# y[1]="kiwi"
# x=tuple(y)
#
# fruits=("olma","anor","uzum")
# mytuple=fruits * 2
# print(mytuple)
# thistuple=(1,3,7,8,5,4,6,8,5)
# x=thistuple.count(5)
# print(x)
#
# thistuple=("olma","anor","urik")
# print(thistuple)
# y=("sariq",)
# thistuple += y
# print(thistuple)
# fruits=("olma","urik","olcha","mandarin","tarvuz")
# (yashil,sariq, *qizil)=fruits
# print(yashil)
# print(sariq)
# print(qizil)
#
# tuple1=("a","b","c")
# tuple2=(1,2,3)
# tuple3=tuple1+tuple2
# print(tuple3)
#
# fruits=("olma","urik","olcha")
# mytuple=fruits * 2
# print(mytuple)
#
# thistuple=(1,3,7,8,7,5,4,6,8,5)
# x=thistuple.index(8)
# print(x)
# yosh=int(input("Yoshingiz nechida?"))
# if yosh>=18:
#     print("Hush kelipsiz!")
# else:
#     print("Sizga kirish mumkin emas!")
# thistuple=("apple","banana","cherry")
# for x in thistuple:
#     print(x)
# thistuple=["olma","anor","uzum"]uzunligi
# print(len(thistuple))
# zeros=[i**2 for i in range (10)]
# print(zeros)
# squares=[]
# for x in range(10):
#     squares.append(x**2)
#     print(squares)t(input(b))
# a=int(input("son kiriting"))
# b=int(input("son kiriting"))
# print(a+b)
# ism=input("Ismingizni kiriting:")
# print("Assalomu alekum," + ism.title())
# mehmonlar=["Ali","Jasur","Nortoy","Nurbek"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}", "sizni ertalabki naxorgi oshga taklif qilamiz")
#     print("Hurmat bilan Fayzullayevlar xonadon
# mehmonlar=["Ali","Sobir","Nurbek","Akbar"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon},sizni ertalabki naxorgi oshga taklif qilamiz")
#     print("Hurmat bilan Fayzullayevlar xonadoni")
# dustlar=["Alisher","Nuriddin","Akbar","Sardor"]
# for dust in dustlar:
#     print(f"Dustim {dust},bugun oshga boramizmi?")
#     print("Bugun dam olaylik")
# t_yil=int(input("Tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# # print("siz:"+str(yosh)+"yoshda ekansiz")
# mehmonlar=["Ali","Vali","Nodir","Shavkat","Ibroxim"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon},sizni navruz bayramiga taklif qilamiz")
#     print("Hurmat bilan dusting Nuriddin")

# t_yil=int(input("Tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("Siz"+str(yosh)+"yoshda ekansiz")
# dustlar=["ali","aziz","donyor","tolik"]
# for dust in dustlar:
#     print(f"Hurmatli {dust}","sizni tugulgan kunimga taklif qilaman")
#     print("hurmat bilan dustingiz nuriddin")
# t_yil=int(input("Tug'ilgan yilingizni kiting:"))
# yosh=2023-t_yil
# # print("Siz,"+str(yosh)+"yoshda ekansiz")
# squares=[]
# for x in range(10):
#     squares.append(x**2)
# print(squares)
# n=int(input())
# lines=[input() for _ in range(n)]
# print(lines)
# t_yil=int(input("tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("siz," + str(yosh) + "yoshda ekansiz")
# ism=input('Ismingiz nima?\n>>>')
# if ism.lower() != 'Nuriddin':
#     print(f"Uzr {ism.title()} biz Nuriddinni kutyammiz")
# else:
#     print("Salom Nuriddin")
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else: # ask holda
#     print('Kirish mumkin emas!')
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:  # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper())  # avto nomini hamma harflarini katta bilan yoz.
#     else:  # aks holda ...
#         print(avto.title())  # avto nomini faqat birinchi harfini katta bilan yoz

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000  # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# # Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:  # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:  # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:  # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:  # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
#
# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
#
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
#
# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")
#
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)
#
# t_yosh=int(input("Tug'ilgan yilingizni kiriting:"))
# yosh=2023-t_yosh
# print("Siz,"+str(yosh)+"yoshda ekansiz")
#
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

#
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}}
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#
# t_yosh=int(input("tugilgan yilimgizni kiriting:"))
# yosh=2023-t_yosh
# print("siz,"+str(yosh)+"yoshda ekansiz")
#
# mehmonlar=["Ali","Nuriddin","Aktam","Ali"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli,{mehmon} sizni tug'ilgan kunga taklif qilamiz")
#     print("Hurmat bilan,Madiyevlar honadoni")
#
# ism = input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
# else:
#     print("Salom, Ali")
#
# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')
#
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2023-yil<18:
#     print(f"Yoshingiz {2023-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")
#
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m'
#
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")
#
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh!")
#
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# phone=telefonlar['ali']
# print(f"Alining telfoni {phone}")
#
# phone=telefonlar['vali']
# print(f"Valining telefoni {phone}")
#
# phone=telefonlar['olim']
# print(f"Olimning telefoni {phone}")
#
# phone=telefonlar['orif']
# print(f"Orifning telefoni {phone}")
#
# t_yil=int(input("tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("siz,"+ str(yosh)+"yoshda ekansiz")

# thisdict={
#     "brand": "Ford",
#     "Model": "Mustang",
#     "year": 1964
# }
# print(thisdict)
# print(thisdict["brand"])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)
#
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict["colors"][0])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["brand"]
# print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.get("brand")
# print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# print(thisdict["colors"][-1])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#     print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(thisdict[x])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.values():
#     print(x)
#
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#     print(x, y)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(len(thisdict))
#
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "somedigits": [1, 2, 3, 4, 5, 6, 7]
# }
# print(len(thisdict))
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
#
# print(thisdict)
#
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
#
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily['child3'])
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)
#
# t_yil=int(input("tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("siz,"+str(yosh)+"yoshda ekansiz")
#
# mehmonlar=["Akbar","Xueshid","Zuhriddin","Nuriddin","Alisher"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli,{mehmon} sizni kechki dasturxonimizga taklif qilamiz")
#     print("Hurmat bilan Nuriddin akayezzi honadoni")
#
# a={}
# b=dict()
# print("a=",a)
# print("b=",b)
#
# thisdict={
#     "brand":"ford",
#     "model":"mustrang",
# }
# print(thisdict)
# print(thisdict["brand"])
#
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964,
#     "year":2020
# }
# print(thisdict)
#
# thisdict={
#     "brand":"ford",
#     "electric":False,
#     "year":1964,
#     "colors":["red","white","blue"]
# }
# print(thisdict["colors"][2])
#
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# print(thisdict["model"])
#
# thisdict={
#     "brand":"ford",
#     "electric":False,
#     "year":1964,
#     "colors":["red","white","blue"]
# }
# print(thisdict["colors"][-2])
#
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# for x in thisdict:
#     print(x)
#
# thisdict={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }
# for x in thisdict.keys():
#     print(x)
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#     print(thisdict[x])

#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
#
# myfamily= {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#                 "name" : "Linus",
#                 "year" : 2011
#               }
# }
# print(myfamily)
#
# mehmonlar=["Ali","Akbar","Nuriddin"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}")
#     print("Sizni kechki dasturxonimizga taklif qilamiz")
#     print("Hurmat bilan do'stingiz Nuriddin")
#
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2020-yil<18:
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#      print("Xush kelibsiz!
#
# mashina0={
#      'model':'lasetti',
#      'rang':'oq',
#      'yil':2020,
#      'narh':11000,
#      'km':5500,
#      'karobka':'avtomat'
#  }
# mashina1={
#      'model':'nexia',
#      'rang':'qizil',
#      'yil':2021,
#      'narh':9000,
#      'km':10000,
#      'karobka':'mexanika'
#  }
# mashina2={
#      'model':'jentra',
#      'rang':'qora',
#      'yil':2017,
#      'narh':15000,
#      'km':5000,
#      'karobka':'avtomat'
#  }
# mashina = mashina0
# print(f"{mashina['model'].title()},\
#    {mashina['rang']} rang,\
#    {mashina['yil']}-yil, {mashina['narh']}$")
#
# mashina = mashina1
# print(f"{mashina['model'].title()},\
#    {mashina['rang']} rang,\
#    {mashina['yil']}-yil, {mashina['narh']}$")
#
# mashina = mashina2
# print(f"{mashina['model'].title()},\
#    {mashina['rang']} rang,\
#    {mashina['yil']}-yil, {mashina['narh']}$")
#
# t_yil=int(input("Tugilgan yilingizni kiriting:"))
# yosh=2023-t_yil
# print("siz,"+str(yosh)+"yoshda ekansiz"
#
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
#
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')
#
# t_yil=int(input("tugilgan yilingizni kiriting"))
# yosh=2023-t_yil
# print("siz,"+str(yosh)+"yoshda ekansiz")
#
# dustlar=['Nuriddin','Akbar','Alisher','Nurbek','Sherzod']
# for dust in dustlar:
#     print(f"Hurmatli,{dust}")
#     print("Sizni kechki dasturhonimzga taklif qilamiz")
#     print("Hurmat bilan do'stingiz Nuriddin")
#
# thisdict={
#     "brand": "Ford",
#     "Model": "Mustang",
#     "year": 1964,
#     "karobka":"Mexanik",
#     "salon":"super"
# }
# thisdict["colors"]="red"
# print(thisdict)
#
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)
#
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
#
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
#
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 8:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")
#
# sonlar = list(range(1,50))
# for son in sonlar:
#     if son == 8:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")
#
# ismlar=[]
# print("Yaqin dustlaringiz ruyxatini tuzamiz.")
# n=1
# while True:
#     savol= f"{n}-dustlaringiz ismini kiriting:"
#     ism=input(savol)
#     ismlar.append(ism)
#     javob=input("Yana ism qushasizmi?  (ha/yo'q)")
#     if javob== 'ha':
#         n+=1
#         continue
#     else:
#         break
#
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# print("Dustlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingizni ismini kiriting:")
#     yosh=input(f"{ism.title()}ning yoshini kiriting:")
#     dostlar[ism]=int(yosh)
#     javob=input("Yana ma'lumot kiritasizmi? (ha/yo'q)")
#     if javob=="yo'q":
#         ishora=False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
#
# def salom_ber ():
#     """salom beruvchi funksiya"""
#     print("assalomu alekum!")

t_yil=int(input("tugilgan yilingizni kiriting:"))
yosh=2023-t_yil
print("siz,"+str(yosh)+"yoshda ekansiz")












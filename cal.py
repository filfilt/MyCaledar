#==============================//==================
a=int(input("የ ዘ መ ኑን ወንጌላዊ ማወቅ ይፈልጋሉን? እባኮን ዓመተ ምህረቱን ያስግቡ?"))
af = 5500
aa = a + af     # ዓመተ ዓለም
b = (a+af)%4    # ወንጌላዊ
d =((a+af)-b)/4 # መጠነ ራዔት
e = (aa+d)%7     # ቅዱስ ዮሀንስ
f=(a+af)%19     # መደብ
g=f-1           # ወንበር
h=g*19%30       # መጥቅ
#==========================//====================
#ወንጌላዊ
if b>=3:
    print('ዘ መ ኑ "ሉ ቃ ስ" ነው')
elif b>=2:
    print('ዘ መ ኑ "ማ ር ቆ ስ" ነው')
elif b>=1 :
    print('ዘ መ ኑ "ማ ቲ ዎ ስ" ነው')
else :
    print('ዘ መ ኑ "ዮ ሀ ን ስ" ነው')
#========================//====================
#ቅዱስዮሀንስ
if e>=6:
    print('የዘመኑ ቅዱስዮህንስ "እሁድ" ይውላል')
elif e>=5:
    print('የዘመኑ ቅዱስዮህንስ "ቅዳሜ" ይውላል')
elif e>=4 :
    print('የዘመኑ ቅዱስዮህንስ "አርብ" ይውላል')
elif e>=3:
    print('የዘመኑ ቅዱስዮህንስ "ሀሙስ" ይውላል')
elif e>=2 :
    print('የዘመኑ ቅዱስዮህንስ "ሮቡዕ" ይውላል')
elif e>=1:
    print('የዘመኑ ቅዱስዮህንስ "ማክሰኞ" ይውላል')
else :
    print('የዘመኑ ቅዱስዮህንስ "ሰኞ" ይውላል')
#======================//=========================
#መጥቅ
# for n in range(53):
if h>=15:
    m=h
    print("መስክሪት " ) 
    print(m)

else :
    m=h+30
    print("ጥቅምት " ) 
    print(m%30)
#-------------------//----------------
if m%7>=6:
    print('"እሁድ"')
elif m%7>=5:
    print(' "ቅዳሜ" ')
elif m%7>=4 :
    print(' "አርብ"')
elif m%7>=3:
    print('"ሀሙስ"')
elif e>=2 :
    print(' "ሮቡዕ" ')
elif m%7>=1:
    print('"ማክሰኞ" ')
else :
    print(' "ሰኞ" ')
#===========================//=====================
#መባጃ ሀመር
if m%7>=6:
    print('"እሁድ"')
elif m%7>=5:
    print()
elif m%7>=4 :
    print(' "አርብ"')
elif m%7>=3:
    print('"ሀሙስ"')
elif e>=2 :
    print(' "ሮቡዕ" ')
elif m%7>=1:
    print('"ማክሰኞ" ')
else :
    print(' "ሰኞ" ')
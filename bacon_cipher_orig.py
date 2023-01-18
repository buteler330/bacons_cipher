import random
print("require two arguments:  plaintext and covertext")
print("WARNING: covertext's length should be strictly 5 times longer than the plaintext(or it gonna result in misdecrypted).space are allowed and will not count in length. no limitation on case")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def inp():
        plaintext=input("plaintext: ")
        covertext=input("covertext(length should be 5 times longer than plaintext's length): ")
        covertext_test=covertext.replace(" ","")
        return plaintext,covertext,covertext_test
def test(plaintext,covertext_test):
    if (len(plaintext)!=(len(covertext_test))/5):
        print("wrong length")
        print(f"[length of plaintext=]={len(plaintext)}")
        print(f"[length of covertext=]={len(covertext_test)}")
        return False
    else:
        return True
# **因为不希望密码本里有重复部分，然后2^5=32,26个元素，很难没有，所以打算封装成函数，调用，if验证
def gen_key_map():
        str=''
        for j in range(5):
            index=random.randint(0,1)
            str+=key_source[index]
        return str
while True:
    plaintext,covertext,covertext_test=inp()
    plaintext=plaintext.replace(" ","")
    plaintext=plaintext.lower()
    flag=test(plaintext,covertext_test)
    if flag==True:
        break
    else:
        continue
key_map=[]
key_source=["a","b"]
# 生成随机密码本
i=0
while i<26:
    str=gen_key_map()
    if str in key_map:
        continue
    else:
        key_map.append(str)
        i+=1
# 转换plaintext
trans_plain=''
for h in range(len(plaintext)):   
    position=alpha.index(plaintext[h])
    trans_plain+=key_map[position]
print("trans_plain:")
print(trans_plain)
cou=0
cipher=''
while cou <len(covertext):
    for u in range(len(trans_plain)):
        if covertext[cou]==' ':
            cipher+=" "
            cou+=1
            if trans_plain[u]=="b":
                cipher+=covertext[cou].upper()
                cou+=1
            else:
                cipher+=covertext[cou].lower()
                cou+=1
        else:
            if trans_plain[u]=="b":
                cipher+=covertext[cou].upper()
                cou+=1
            else:
                cipher+=covertext[cou].lower()
                cou+=1
print(f"[key map===>]{key_map}")
print(f'[cipher===>][{cipher}]')

# 因为covertext是随机生成的，所以不能添加空格，然而遍历的时候又是以原文的长度进行遍历，所以出现空格的时候会导致二者对应的错位，所以将每个计数器都单分出来
# 原本的和后来改的随机covertext的不一样，因为本来原文是没有空格的，而covertext有，但后来变成了，原文里有，covertext随机生成，所以没有










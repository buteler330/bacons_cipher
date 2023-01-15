import random
print("require two arguments:  plaintext and covertext")
print("WARNING: covertext's length should be strictly 5 times longer than the plaintext(or it gonna result in misdecrypted).space are allowed and will not count in length. no limitation on case")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
plaintext=''
covertext=""
def inp():
    global plaintext,covertext
    plaintext=input("plaintext: ")
    covertext=input("covertext(length should be 5 times longer than plaintext's length): ")
inp()
plaintext=plaintext.replace(" ","")
plaintext=plaintext.lower()
covertext_test=covertext.replace(" ","")
if (len(plaintext)!=(len(covertext_test))/5):
    print("wrong length")
    print(f"[length of plaintext=]={len(plaintext)}")
    print(f"[length of covertext=]={len(covertext)}")
    inp()

# print(len(plaintext))
# print(plaintext)
key_map=[]
key_source=["a","b"]

# **因为不希望密码本里有重复部分，然后2^5=32,26个元素，很难没有，所以打算封装成函数，调用，if验证
def gen_key_map():
        str=''
        for j in range(5):
            index=random.randint(0,1)
            str+=key_source[index]
        # print(str)
        return str
# 生成随机密码本
i=0
while i<26:
    str=gen_key_map()
    if str in key_map:
        continue
    else:
        key_map.append(str)
        i+=1
# print(key_map)
# print(len(key_map))
trans_plain=''
for h in range(len(plaintext)):
    position=alpha.index(plaintext[h])
    # print(position)
    trans_plain+=key_map[position]
print("trans_plain:")
print(trans_plain)
trans_cover=''
cou=0
while cou<len(covertext) :
    for u in range(len(trans_plain)):
        if covertext[cou]==" ":
            trans_cover+=" "
            cou+=1
            if trans_plain[u]=="b":
                trans_cover+=covertext[cou].upper()
                cou+=1
            else:
                trans_cover+=covertext[cou].lower()
                cou+=1
            continue
        else:
            if trans_plain[u]=="b":
                trans_cover+=covertext[cou].upper()
                cou+=1
            else:
                trans_cover+=covertext[cou].lower()
                cou+=1
print(f"[key map===>]{key_map}")
print(f'[cipher===>][{trans_cover}]')














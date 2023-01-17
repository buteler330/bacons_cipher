import random
print("plaintext can only contain letter and space. not number or other punctuation")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
plaintext=''
plaintext=input("plaintext: ")
plaintext_test=plaintext.replace(" ","")
plaintext=plaintext.lower()
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
print(key_map)
# 转换plaintext
trans_plain=''
for h in range(len(plaintext)):
    if plaintext[h]==" ":
        trans_plain+=" "
    else:   
        position=alpha.index(plaintext[h])
        trans_plain+=key_map[position]
print("trans_plain:")
print(trans_plain)
# 生成随机cover文本
covertext=''
for ind in range(5*len(plaintext_test)):
    covertext+=alpha[random.randint(0,25)]
print(f'covertext{covertext}')
# 生成密文
cou=0
covertext_count=0
cipher=''
while cou<len(trans_plain):
    if trans_plain[cou]==" ":
        cipher+=" "
        cou+=1
        if trans_plain[cou]=="b":
            cipher+=covertext[covertext_count].upper()
            cou+=1
            covertext_count+=1
        else:
            cipher+=covertext[covertext_count].lower()
            cou+=1
            covertext_count+=1
        continue
    else:
        if trans_plain[cou]=="b":
            cipher+=covertext[covertext_count].upper()
            cou+=1
            covertext_count+=1
        else:
            cipher+=covertext[covertext_count].lower()
            cou+=1
            covertext_count+=1
print(f"[key map===>]{key_map}")
print(f'[cipher===>][{cipher}]')

# 因为covertext是随机生成的，所以不能添加空格，然而遍历的时候又是以原文的长度进行遍历，所以出现空格的时候会导致二者对应的错位，所以将每个计数器都单分出来













key_map=input("key_map:")
key_map=eval(key_map)
cipher=input("cipher:")
cipher_rip=cipher.replace(" ","")
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
trans_5_list=[]
trans_ab=''
plaintext=""
cipher_i=0
while cipher_i < len(cipher_rip):
    str=''
    for i in range(5):
        str+=cipher_rip[cipher_i+i]
    cipher_i+=5
    trans_5_list.append(str)
print(trans_5_list)
for ele in trans_5_list:
        for count in range(5):
            if ele[count]<'a':
                trans_ab+="b"
            else:
                trans_ab+="a"
print(trans_ab)
count_5=0
while count_5<len(trans_ab):
    str=''
    for i in range(5):
        str+=trans_ab[count_5+i]
    # print(str)
    count_5+=5
    ind=key_map.index(str)
    # print(ind)
    plaintext+=alpha[ind]
print(plaintext)
















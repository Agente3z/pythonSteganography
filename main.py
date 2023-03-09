def crypt(fileName,stringa):

    file = open(fileName,"r+b")
    data = file.read()

    lenght = data[18]
    height = data[22]

    if len(stringa) > height-1:
        return 0
    
    msg = [bin(ord(i))[2:] for i in stringa]
    lunghezza = bin(len(stringa))[2:]

    index = 54+lenght*3-7
    
    while len(lunghezza)<7:
        lunghezza = "0"+lunghezza

    for b in lunghezza:
        byte = data[index]
        byte = byte&254 if b == "0" else byte|1
        if byte<16:
                byte = "0"+hex(byte)[2:]
        else:
            byte = hex(byte)[2:]
        file.seek(index)
        file.write(bytes.fromhex(byte))
        index+=1
    
    for i in range(len(msg)):
        while len(msg[i])<7:
            msg[i] = "0"+msg[i]    

    for by in msg:
        index += lenght*3 - 7
        for b in by:
            byte = data[index]
            byte = byte&254 if b == "0" else byte|1
            if byte<16:
                byte = "0"+hex(byte)[2:]
            else:
                byte = hex(byte)[2:]
            file.seek(index)
            file.write(bytes.fromhex(byte))
            index+=1
    
    file.close()
    return 1

def decrypt(fileName):
    with open(fileName,"rb") as f:
        data = f.read()
    
    lenght = data[18]

    lunghezza = ""
    index=54+lenght*3-7

    for _ in range(7):
        byte = bin(data[index])[2:]
        lunghezza+=byte[-1]
        index+=1
    
    msg = ""
    lunghezza = int(lunghezza,2)
    for _ in range(lunghezza):
        index += lenght*3 - 7
        char = ""
        for _ in range(7):
            byte = bin(data[index])[2:]
            char+=byte[-1]
            index+=1
        msg += chr(int(char,2))
    
    return msg

scelta = input("0) Encode\n1) Decode\n> ")

if scelta=="0":
    fileName = input("Enter file name: ")
    stringa = input("Enter message to hide: ")
    res = crypt(fileName,stringa)
    print("Message encoded") if res==1 else print("Message is too big")
    
elif scelta=="1":
    fileName = input("Enter file name: ")
    msg = decrypt(fileName)
    print(msg)
def Encrypt(lettr, shift):
    indx = ord(lettr)
    if 65 <= indx <= 90:
        indx -= 65
        indx = (indx + shift)%26
        indx += 65
    elif 97 <= indx <= 122:
        indx -= 97
        indx = (indx + shift)%26
        indx += 97
    return chr(indx)

def NormlShift(shift, dcrpt):
    if 97 <= shift <= 122:
        shift -= 32
    shift -= 65
    if dcrpt:
        shift *= -1
    return shift

def CaesarCiph(key, message, decrypt):
    encr = ''
    shift = NormlShift(ord(key[0]), decrypt)
    for i in message:
        encr += Encrypt(i, shift)
    return encr

def ViginereCiph(key, message, decrypt):
    encr = ''
    keylen = len(key)
    cnt = 0
    for i in message:
        ordnung = ord(i)
        if ordnung < 65 or 90 < ordnung < 97 or 122 < ordnung:
            encr += i
            continue
        shift = NormlShift(ord(key[cnt]), decrypt)
        encr += Encrypt(i, shift)
        cnt += 1
        if cnt >= keylen:
            cnt = 0
    return encr

def VernamCiph(key, message, decrypt):
    encr = ''
    keylen = len(key) - 1
    cnt = 0
    for i in message:
        ordnung = ord(i)
        if ((ordnung < 65 or 90 < ordnung < 97 or 122 < ordnung) and not decrypt) or ((ordnung < 65 or 96 < ordnung) and decrypt):
            encr += i
            continue  
        ciph = (NormlShift(ord(i), False))^(NormlShift(ord(key[cnt]), False))
        cnt += 1
        if cnt >= keylen:
            cnt = 0
        ciph += 65
        encr += chr(ciph)
    return encr;

def CrackCaesar(message):
    cash = []
    decr = []
    stat = [0]*26
    cnt = 0
    for i in message:
        lettr = NormlShift(ord(i), False)
        if (0 <= lettr <= 25):
            stat[lettr] += 1
            cnt += 1
    for i in range(26):
        stat[i] *= 100/cnt
    freq = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6,97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.07]
    for i in range(26):
        indx = 0
        min = 101
        for j in range(26):
            if abs(freq[i] - stat[j]) < min:
                min = abs(freq[i] - stat[j])
                indx = j
        shift = i - indx
        if shift in cash:
            continue
        cash.append(shift);
        encr = ''
        for k in message:
            encr += Encrypt(k, shift)
        decr.append((-shift, encr))
    return decr
        
        

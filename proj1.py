import argparse
parser = argparse.ArgumentParser(
    prog='Simple ciphers',
    description='Choose cipher and encrypt/decrypt mode using following cmd args, give the input and output files paths',
    epilog='Friesen Artem B05-206'
)
parser.add_argument('-c', '--cipher', choices=['csr', 'vgnr', 'vrnm', 'crck'], help='choose the Caesar, Viginere, Vernam cipher or cracking Caesar cipher mode')
parser.add_argument('-d', '--decrypt', action='store_true', help='Use this flag to decrypt cipher')
parser.add_argument('-i', '--input', nargs='?', default='input.txt', help='give the path to input file, in input file give key in first line and message in second line')
parser.add_argument('-o', '--output', nargs='?', default='output.txt', help='give the path to output file, there will be message and shift number if you chosen crck mode')
args = parser.parse_args()

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

inp = open(args.input)
if (args.cipher != 'crck'):
    key = inp.readline()
message = inp.read()
inp.close()
outp = open(args.output, 'w')

if args.cipher == 'csr':
    shift = NormlShift(ord(key[0]), args.decrypt)
    for i in message:
        outp.write(Encrypt(i, shift))
    outp.write('\n')
    
elif args.cipher == 'vgnr':
    keylen = len(key)
    cnt = 0
    for i in message:
        ordnung = ord(i)
        if ordnung < 65 or 90 < ordnung < 97 or 122 < ordnung:
            outp.write(i)
            continue
        shift = NormlShift(ord(key[cnt]), args.decrypt)
        outp.write(Encrypt(i, shift))
        cnt += 1
        if cnt >= keylen:
            cnt = 0
    outp.write('\n')

elif args.cipher == 'vrnm':
    keylen = len(key)
    cnt = 0
    for i in message:
        ordnung = ord(i)
        if ((ordnung < 65 or 90 < ordnung < 97 or 122 < ordnung) and not args.decrypt) or ((ordnung < 65 or 96 < ordnung) and args.decrypt):
            outp.write(i)
            continue  
        ciph = (NormlShift(ord(i), False))^(NormlShift(ord(key[cnt]), False))
        cnt += 1
        if cnt >= keylen:
            cnt = 0
        ciph += 65
        outp.write(chr(ciph))
    outp.write('\n')
else:
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
        for k in message:
            outp.write(Encrypt(k, shift))
        outp.write(' shift = ')
        outp.write(str(shift))
        outp.write('\n')
outp.close()




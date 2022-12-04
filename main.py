import ciphs
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

inp = open(args.input)
if (args.cipher != 'crck'):
    key = inp.readline()
message = inp.read()
inp.close()
outp = open(args.output, 'w')

decrypt = args.decrypt

if args.cipher == 'csr':
    encr = ciphs.CaesarCiph(key, message, decrypt)
    outp.write(encr)
    outp.write('\n')

elif args.cipher == 'vgnr':
    encr = ciphs.ViginereCiph(key, message, decrypt)
    outp.write(encr)
    outp.write('\n')
    
elif args.cipher == 'vrnm':
    encr = ciphs.VernamCiph(key, message, decrypt)
    outp.write(encr)
    outp.write('\n')
else:
    decr = ciphs.CrackCaesar(message)
    for i in range(len(decr)):
        outp.write(decr[i][1])
        outp.write('\n shift = ')
        outp.write(str(decr[i][0]))
        outp.write('\n\n')
outp.close()

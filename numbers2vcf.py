from time import sleep
print('''
Welcome ...

    Programmed by : Dr.Adel Mahmoud
    Facebook      : https://www.facebook.com/adel13013
    github        : https://github.com/AdelMahmoudHussein
    version       : 1.0
    Name          : convert numbers to Vcard

==================================================
Steps:
    1-you must type full path of file if not in the same directory
    2-type numbers file name with extention like "numbers.txt"
    3-numbers without plus "+"  
    4-output file name is "names-numbers.vcf"
''') 

n = 10001
filename = input ('Enter numbers file name with extention: ')
with open('names-numbers.vcf','w') as vcf:
    with open(filename) as txt:
        for t in txt:
            tt=str(t).rstrip('\n')
            c = 'AM' + str(n) + '-' + tt + ',' + '+' + tt 
            cc = 'BEGIN:VCARD\n' + 'VERSION:3.0\n' 
            cc = cc + 'N:' + 'AM' + str(n) + '-' + tt + ';;;\n'
            cc = cc + 'FN:' + 'AM' + str(n) + '\n'
            cc = cc + 'TEL;TYPE=VOICE,CELL;VALUE=text:' + '+' + tt + '\n'
            cc = cc + 'END:VCARD'
            print(cc, file=vcf)
            n+=1
            
print('\nDone\n')
print('3 seconds to exit')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('0')


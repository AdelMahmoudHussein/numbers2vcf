from time import sleep
print('''
Welcome ...

    Programmed by : Dr.Adel Mahmoud
    Facebook      : https://www.facebook.com/adel13013
    github        : https://github.com/AdelMahmoudHussein
    version       : 1.1
    Name          : convert numbers to Vcard

==================================================
Steps:
    1-you must type full path of file if not in the same directory
    2-type numbers file name with extention like "numbers.txt"  
    3-text file encoding must be utf-8 
''') 

filename = input ('Enter numbers file name with extention: ')
prefix = input ('Enter character to start with as Prefix : ')
n = int(input('Enter Number to start from : '))
with open(filename[0:-4]+'.vcf','w') as vcf:
    with open(filename) as txt:
        for t in txt:
            if len(t)> 3 :    
                tt=str(t).strip()
                tt = tt.lstrip('+')
                c = prefix + str(n) + '-' + tt + ',' + '+' + tt 
                cc = 'BEGIN:VCARD\n' + 'VERSION:3.0\n' 
                cc = cc + 'N:' + prefix + str(n) + '-' + tt + ';;;\n'
                cc = cc + 'FN:' + prefix + str(n) + '\n'
                cc = cc + 'TEL;TYPE=VOICE,CELL;VALUE=text:' + '+' + tt + '\n'
                cc = cc + 'END:VCARD'
                print(cc, file=vcf)
            n+=1
            
print('\nDone\n\n')
input('Enter any character to exit : ')
print('3 seconds to exit')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('0')


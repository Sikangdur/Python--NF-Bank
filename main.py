import random, string
print("***** SELAMAT DATANG DI NF BANK *****")



#MENU UTAMA
def menu_utama():
    print()
    print("MENU:")
    print("[1] Buka rekening")
    print("[2] Setoran tunai")
    print("[3] Tarik tunai")
    print("[4] Transfer")
    print("[5] Lihat daftar transfer  ")
    print("[6] Keluar")

#FITUR BUKA REKENING
def buka_rekening():
    nama_nasabah = input('Masukkan nama anda : ')
    setoran_awal = input('Masukkan setoran awal : ')
    data_nasabah = norek + ',' + nama_nasabah + ',' + setoran_awal
    f = open('nasabah.txt', 'a+')
    f.write(data_nasabah + '\n')
    f.close()
    print('Pembukaan rekening dengan nomor', norek,
          'atas nama', nama_nasabah, 'berhasil.')

#FITUR SETORAN TUNAI
def setoran_tunai(norek, nominal_setoran):
    f = open('nasabah.txt', 'r')
    data_setoran = f.readlines()
    for i in range(len(data_setoran)):
        ls = data_setoran[i].split(',')

        if (norek == ls[0]):
            saldo = int(ls[2])
            ls[2] = saldo + nominal_setoran
            data_setoran[i]  = ls[0] + ',' + ls[1] + ',' + str(ls[2]) + '\n'
            f = open('nasabah.txt', 'w+')
            data_setoran = f.writelines(data_setoran)
            return 'Setoran tunai sebesar ' + str(nominal_setoran) + ' ke rekening ' + str(norek) + ' berhasil '
        else:
            pass
    return 'Nomor rekening tidak terdaftar. Setoran tunai gagal.'

#FITUR TARIK TUNAI
def tarik_tunai(norek, nominal_tarik):
    f = open('nasabah.txt', 'r')
    data_tarik = f.readlines()
    for i in range(len(data_tarik)):
        ls = data_tarik[i].split(',')

        if (norek == ls[0]):
            saldo = int(ls[2])
            if (saldo < nominal_tarik):
                return 'Saldo tidak mencukupi. Transaksi gagal.'
            else:
                ls[2] = saldo - nominal_tarik
                data_tarik[i] = ls[0] + ',' + ls[1] + ',' + str(ls[2]) + '\n'
                f = open('nasabah.txt', 'w+')
                data_tarik = f.writelines(data_tarik)
                return 'Tarik tunai sebesar ' + str(nominal_tarik) + ' dari rekening ' + str(norek) + ' berhasil '
        else:
            pass
    return 'Nomor rekening tidak terdaftar. Tarik tunai gagal.'
#FITUR TRANSFER
def transfer(kodetrans, rek_sumber, rek_tujuan, nominal_tf):
    f = open('nasabah.txt', 'r')
    data_tarik = f.readlines()
    data_setor = f.readlines()
    for i in range(len(data_tarik)):
        ls = data_tarik[i].split(',')

        if (rek_sumber == ls[0]):
            saldo = int(ls[2])
            if (saldo < nominal_tf):
                return 'Saldo tidak mencukupi. Transaksi gagal.'
            else:
                ls[2] = saldo - nominal_tf
                data_tarik[i] = ls[0] + ',' + ls[1] + ',' + str(ls[2]) + '\n'
                f = open('nasabah.txt', 'w+')
                data_tarik = f.writelines(data_tarik)

                data_transfer = kodetrans + ',' + rek_sumber + ',' + rek_tujuan + ',' + str(nominal_tf) + '\n'
                trans = open('transfer.txt', 'a+')
                data_transfer = trans.writelines(data_transfer)
                return "Sukses"
        
        elif (norek == ls[0]):
            saldo = int(ls[2])
            ls[2] = saldo + nominal_tf
            data_setor[i]  = ls[0] + ',' + ls[1] + ',' + str(ls[2]) + '\n'
            f = open('nasabah.txt', 'w+')
            data_setor = f.writelines(data_setor)
            return 'Transfer sebesar '+str(nominal_tf)+' dari rekening '+rek_sumber+' ke rekening '+rek_tujuan+' berhasil.'

        elif (norek == norek):
            return 'Silahkan tulis nomor rekening tujuan yang berbeda '

        else:
            pass

    return 'Nomor rekening tidak terdaftar. Transfer gagal.'

#FITUR KIHAT DAFTAR TRANSFER
def daftar_transfer(sumber):
    list_transfer = []
    f = open('transfer.txt')
    for each_line in f:
        data = each_line.split(',')
        a = data[0]
        b = data[1]
        c = data[2]
        d = data[3]
        if(b == sumber):
            print([a,b,c,d])
        else:
            pass

    for i in range(len(list_transfer)):
        for j in range(len(list_transfer[i])):
            print(list_transfer[i][j])

    f.close()

menu_utama()
while True:
    menu = input('Masukkan menu pilihan Anda : ')
    norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
    kodetrans = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
    if menu == '1':
        print()
        print('*** BUKA REKENING ***')
        buka_rekening()
        menu_utama()

    elif menu == '2':
        print()
        print('*** SETORAN TUNAI ***')
        norek = input('Masukkan nomor rekening : ').upper()
        nominal_setoran = int(input('Masukkan nominal yang akan disetor : '))
          
        print(setoran_tunai(norek, nominal_setoran))
        menu_utama()

    elif menu == '3':
        print()
        print('*** TARIK TUNAI ***')
        norek = input('Masukkan nomor rekening : ').upper()
        nominal_tarik = int(input('Masukkan nominal yang akan ditarik : '))
        print(tarik_tunai(norek, nominal_tarik))
        menu_utama()

    elif menu == '4':
        print()
        print('*** TRANSFER ***')      
        rek_sumber = input('Masukkan nomor rekening sumber : ').upper()
        rek_tujuan = input('Masukkan nomor rekening tujuan : ').upper()
        nominal_tf = int(input('Masukkan nominal yang akan ditransfer : '))
        print(transfer(kodetrans, rek_sumber, rek_tujuan, nominal_tf))
        setoran_tunai(rek_tujuan, nominal_tf)
        menu_utama()

    elif menu == '5':
        print()
        print('*** LIHAT DATA TRANSFER ***')
        sumber = input('Masukkan nomor rekening sumber transfer:').upper()
        print("Daftar transfer dari rekening", sumber, " :")
        daftar_transfer(sumber)
        menu_utama()

    elif menu == '6':
        print("Terima kasih atas kunjungan Anda...")
        break

    else:
        print('Pilihan anda salah, Ulangi.')
        pass

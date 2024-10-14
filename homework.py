print('POSYANDU BALITA')

nama = input('masukan nama :')
umur = int(input('masukan umur :'))
nik_kartu_keluarga = int(input('masukan nik kartu keluarga :'))
tanggal_lahir = int(input('masukan tanggal lahir:'))
nama_orang_tua = input('Masukan Nama Orang Tua : ')
daerah_posyandu =input('masukan daerah posyandu : ')

list = ['6','7','8','9','10']
if(umur not in list) :
    print('memenuhi')
else :
    print('tidak memenuhi')

print('salam sehat')
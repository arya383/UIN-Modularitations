nama = 'Arya Santri Wiratama'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak,waktu):
    kecepatan = jarak / waktu
    print(f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')

    return kecepatan

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

def Hitung_gaya(massa,percepatan):
    gaya = massa * percepatan
    print(f'massa = {massa / 1000}kg dikenai sebuah percepatan = {1000 / 3600}m/s')
    print(f'sehingga gaya = {gaya} Newton')

gaya = Hitung_gaya(30, 25)



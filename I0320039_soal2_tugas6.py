#PROGRAM MENGHITUNG NILAI RATA-RATA
print("PROGRAM MENGHITUNG NILAI RATA-RATA")

#input batas inputan dari pengguna
banyak_inputan = int(input("Berapa banyak nilai yang ingin anda input: "))
n = 0
listnilai = []

for i in range(0, banyak_inputan):
    nilai = int(input("Masukkan data ke-%d: " % (i+1)))
    listnilai.append(nilai)
    n += listnilai[i]
    #menghitung rata rata
    rata_rata = n / banyak_inputan

#output
print('')
print("Rata-rata  = %f" %rata_rata)
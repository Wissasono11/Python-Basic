# Episode input user

# data yang dimasukkan pasti string
data = input("Masukkan nama: ")

print("Data yang diinputkan = ", data, "type = ", type(data))

# jika kita ingin mengambil int dan float, maka
angka = int(input("Masukkan umur: "))
angka1 = float(input("Masukkan tinggi badan: "))

print("Data yang diinputkan  = ", angka, "type = ", type(angka))
print("Data yang diinputkan = ", angka1, "type = ", type(angka1))

# bagaimana dengan boolean?
biner = bool(int(input("Single atau Duo (jawab dengan 0 atau 1): ")))
print("Data yang diinputkan = ", biner, "type = ", type(biner))
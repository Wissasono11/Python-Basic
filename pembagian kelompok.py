import random

def bagi_kelompok(nama_orang, jumlah_kelompok):
    random.shuffle(nama_orang)
    kelompok = [[] for _ in range(jumlah_kelompok)]
    
    for i, nama in enumerate(nama_orang):
        kelompok[i % jumlah_kelompok].append(nama)
    
    return kelompok

def main():
    # Input nama orang, pisahkan dengan koma (,)
    input_nama = input("Masukkan nama-nama orang (pisahkan dengan koma): ")
    nama_orang = [nama.strip() for nama in input_nama.split(',')]

    # Input jumlah kelompok
    jumlah_kelompok = int(input("Masukkan jumlah kelompok: "))

    # Membagi nama menjadi kelompok
    hasil_kelompok = bagi_kelompok(nama_orang, jumlah_kelompok)

    # Menampilkan hasil
    for i, kelompok in enumerate(hasil_kelompok):
        print(f"Kelompok {i+1}: {', '.join(kelompok)}")

if __name__ == "__main__":
    main()
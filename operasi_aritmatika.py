# operasi aritmatika

a = int(input("Masukkan angka 1: ")) 
b = int(input("Masukkan angka 2: ")) 

# operasi penjumlahan (+)
hasil = a + b
print(a, '+' ,b, '=', hasil)

# operasi pengurangan (-)
hasil = a - b
print(a, '-' ,b, '=', hasil)

# operasi perkalian (*)
hasil = a * b
print(a, '*' ,b, '=', hasil)

# operasi pembagian (/)
hasil = a / b
print(a, '/' ,b, '=', hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**' ,b, '=', hasil) # bilangan a integer di pangkatkan oleh bilangan b integer 

# operasi modulus (%) 
hasil = a % b
print(a, '%' ,b, '=', hasil)

# operasi floor division (//) 
hasil = a // b
print(a, '//' ,b, '=', hasil) # sejenis operator untuk pembulatan angka di belakang koma menjadi bilangan bulat saja
print("===========================")
# prioritas operasi, operational precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)
"""1. dalam kurung() 
   2. pangkat **
   3. perkalian *
   4. pembagian /
   5. modulus %
   6. floor division //
   7. penjumlahan +
   8. pengurangan -"""

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama dalam operasi aritmatika
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)
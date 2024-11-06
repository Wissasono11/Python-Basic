#tipe data adalah macam macam data
# a = 10 , adalah dengan nilai 10

#1. tipe data : angka satuan(integer)
nilai_int = 2
print("data : ", nilai_int) 
print("- bertipe :", type(nilai_int))

#2. tipe data : angka dengan koma(float)
nilai_float = 2.125
print("data : ", nilai_float) 
print("- bertipe :", type(nilai_float))

#3. tipe data : kumpulan karakter(string)
nilai_string = "ASEP BENSIN 11"
print("data : ", nilai_string) 
print("- bertipe :", type(nilai_string))

#4. tipe data : biner true/false(boolean)
nilai_bool = True 
print("data : ", nilai_bool) 
print("- bertipe :", type(nilai_bool))

# tipe data khusus
# -bilangan kompleks
nilai_complex = complex(1,1) #jika dirun maka akan menghasilkan 1+1j dimana j adalah imajiner
print("data : ", nilai_complex) 
print("- bertipe :", type(nilai_complex))

# tipe data dari bahasa C

from ctypes import c_double

nilai_c_double = c_double(20.23)
print("data : ", nilai_c_double) 
print("- bertipe :", type(nilai_c_double))
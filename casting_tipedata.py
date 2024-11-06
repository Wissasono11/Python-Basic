# casting -> merubah dari satu tipe ke tipe lain

# integer
print("=====INTEGER=====")
nilai_int = 11
print("nilai = ", nilai_int, ",type =",type(nilai_int))
# dirubah
nilai_float = float(nilai_int)
nilai_str = str(nilai_int)
nilai_bool = bool(nilai_int) # akan false jika nilai_int = 0
print("nilai = ", nilai_float, ",type =",type(nilai_float))
print("nilai = ", nilai_str, ",type =",type(nilai_str))
print("nilai = ", nilai_bool, ",type =",type(nilai_bool))

# float
print("=====FLOAT=====")
nilai_float = 11.127
print("nilai = ", nilai_float, ",type =",type(nilai_float))
# dirubah
nilai_int = int(nilai_float)
nilai_str = str(nilai_float)
nilai_bool = bool(nilai_float) # akan false jika nilai_float = 0
print("nilai = ", nilai_int, ",type =",type(nilai_int))
print("nilai = ", nilai_str, ",type =",type(nilai_str))
print("nilai = ", nilai_bool, ",type =",type(nilai_bool))

# boolean
print("=====BOOLEAN=====")
nilai_bool = True
print("nilai = ", nilai_bool, ",type =",type(nilai_bool))
# dirubah
nilai_int = int(nilai_bool)
nilai_str = str(nilai_bool)
nilai_float = float(nilai_bool) # akan false jika nilai_float = 0
print("nilai = ", nilai_int, ",type =",type(nilai_int))
print("nilai = ", nilai_str, ",type =",type(nilai_str))
print("nilai = ", nilai_float, ",type =",type(nilai_float))

# string
print("=====STRING=====")
nilai_str = "19"
print("nilai = ", nilai_str, ",type =",type(nilai_str))
# dirubah
nilai_int = int(nilai_str) # string harus angka
nilai_bool = bool(nilai_str) # false jika string kosong
nilai_float = float(nilai_str) # string harus angka
print("nilai = ", nilai_int, ",type =",type(nilai_int))
print("nilai = ", nilai_bool, ",type =",type(nilai_bool))
print("nilai = ", nilai_float, ",type =",type(nilai_float))
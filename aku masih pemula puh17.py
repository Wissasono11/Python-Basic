# Sets(Himpunan) = collection which is unordered, unindexed, and no duplicate values

utensils ={"fork", "spoon", "knife", "plate"}
dishes ={"bowl", "plate", "cup", "knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)

dinners_table = utensils.union(dishes) #union berfungsi untuk gabungan yaitu menggabungkan elemen A dan elemen B ke dalam satu list

print(utensils.difference(dishes)) #berfungsi untuk memprsentasikan elemen yang berbeda antara himpunan satu dengan yang lain
print(dinners_table) #berfungsi untuk memprsentasikan elemen yang berbeda antara himpunan satu dengan yang lain
print(dishes.intersection(utensils)) #intersection berfungsi sebagai irisan untuk setiap elemen yang sama dari suatu himpunan
#for x in dinners_table:
#    print(x)
#saat program dieksekusi maka akan menghasilkan output yang berbeda
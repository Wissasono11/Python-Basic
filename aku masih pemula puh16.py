#tuple = collection which is ordered and unchangeable 
#        used to group together related data

student = ("Bayu", 18, "male", "Bayu")

print(student.count("Bayu")) #count berfungsi untuk menghitung berapa banyak elemen sama yang muncul dalam suatu list
print(student.index("male")) #index berfungsi untuk memposisikan posisi elemen di urutan ke berapa dalam list

for x in student:
    print(x)

if "Bayu" in student:
    print("Bayu is here!")
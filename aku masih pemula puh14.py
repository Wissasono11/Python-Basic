# list = used to store multiple items in a single variable

food = ["mie sedap", "ayam penyet", "soto ayam", "kwetiau","orak arik tempe"]

food[0] = "indomie"
food[1] = "jatinagor"

food.append("es krim")         #append berfungsi menambahkan elemen baru ke dalam list
food.remove("kwetiau")         #remove berfungsi untuk menghapus elemen dari list
food.pop()                     #pop berfungsi untuk menghapus 1 elemen urutan terakhir dari list 
food.insert(2, "tahu gejrot")  #insert berfungsi untuk memasukkan atau menggantikan elemen lama dengan elemen baru dari list
food.sort()                    #sort mengurutkan setiap abjad elemen dari list
food.clear()                   #clear berfungsi untuk menghapus semua elemen dari dalam list
for x in food:
    print(x)
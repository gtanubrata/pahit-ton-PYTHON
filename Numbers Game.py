def menu():

    print("---------\nMAIN MENU\n---------\n"
    "1. Isi List\n"
    "2. Lihat List\n"
    "3. Sort List Ascending\n"
    "4. Sort List Descending\n"
    "5. Nilai Tertinggi dan Terendah\n"
    "6. Jumlah Ganjil dan Genap\n"
    "7. Ulang\n"
    "8. Keluar\n")

#
#
#
storage = []

def isi_list():
    n = int(input("Mau masukkan berapa angka? "))

    for _ in range(n):
        storage.append(int(input("Masukkan angka: ")))

def lihat_list():
    print(storage)

def sort_ascending():
    for i in range(len(storage)):
        for j in range(i+1, len(storage)):
            if storage[i] > storage[j]:
                storage[i], storage[j] = storage[j], storage[i]
    print(storage)

def sort_descending():
    for i in range(len(storage)):
        for j in range(i + 1, len(storage)):
            if storage[j] > storage[i]:
                storage[i], storage[j] = storage[j], storage[i]
    print(storage)

def min_max():
    for i in range(len(storage)):
        for j in range(i+1, len(storage)):
            if storage[i] > storage[j]:
                storage[i], storage[j] = storage[j], storage[i]
    min_value = storage[0]
    max_value = storage[-1]
    print("Nilai terendah adalah {} dan nilai tertinggi adalah {}".format(min_value, max_value))

def ganjil_genap():

    n_ganjil, n_genap = 0, 0

    for i in range(len(storage)):
        if storage[i] % 2 == 1:
            n_ganjil += 1
        else:
            n_genap += 1
    print("Ada {} bilangan ganjil dan {} bilangan genap".format(n_ganjil, n_genap))

def reset():
    storage.clear()
    print("Silahkan isi list lagi..")

#
#
#
loop = True

while loop:
    menu()
    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        isi_list()

    elif pilihan == 2:
        lihat_list()

    elif pilihan == 3:
        sort_ascending()

    elif pilihan == 4:
        sort_descending()

    elif pilihan == 5:
        min_max()

    elif pilihan == 6:
        ganjil_genap()

    elif pilihan == 7:
        reset()

    elif pilihan == 8:
        loop = False
        print("Terima kasih!")

    else:
        print("Salah input, masukkan 1-8 :)")


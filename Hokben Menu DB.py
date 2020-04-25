# PR Hokben with MySQL
# 15 April 2020
# Gabriella JC-DS-JKT-08 no. 3

import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host = 'localhost',
                               user = 'root',
                               passwd = 'password'
                              )

cursor = conn.cursor(dictionary = True)


# global variables:
history = {}
nama = ''
total = 0


def order():
    menu_dict = {1: 'Hoka hemat 1',
                2: 'Hoka hemat 2',
                3: 'Hoka hemat 3'}

    price_dict = {1: 20000,
                2: 25000,
                3: 30000}

    print('''1. Hoka hemat 1: 20000\n2. Hoka hemat 2: 25000\n3. Hoka hemat 3: 30000''')
    
    order = int(input('Beli yang mana? '))
    qty = int(input('Berapa banyak? '))

    history[menu_dict[order]] = [qty, price_dict[order]]
    # constraint: jika order duplicate (1, lalu 1 lagi) akan ketimpa :/
    
    return history


def cart():
    if len(history) > 0:
        for key, val in history.items():
            print('{} banyak {} total {}'.format(key, val[0], val[0]*val[1]))
    else:
        print('Cart kosong')


def checkout():
    global nama
    global total

    
    if len(history) > 0:
        nama = input('Order atas nama ')
        cart()
        
        for val in history.values():
            total += val[0]*val[1]
        print('Total order {} '.format(total))

        return total

    else:
        print('Mohon isi cart')

def update():
    for key, val in history.items():
        str_sql = '''INSERT INTO hokben.hokben (no, namaPembeli, namaPaket, quantity, totalHarga)
                     VALUES(NULL, '{namaPembeli}', '{namaPaket}', '{quantity}', '{totalHarga}');'''
        
        sql_script = str_sql.format(namaPembeli = nama,
                                    namaPaket = key,
                                    quantity = val[0],
                                    totalHarga = val[0] * val[1]
                                    )
        
        cursor.execute(sql_script)
        
        # ubah db dengan permanen
        conn.commit()

def menu():
    
    while(True):
        print('Selamat datang di Hokben!\n1. Lihat menu\n2. Lihat cart\n3. Checkout\n4. Lihat history\n5. Keluar')
        pilih = int(input('Silahkan pilih '))

        if pilih == 1:
            while(True):
                order()
                multi = input('Tambah lagi? [y/n] ')
                if multi != 'y':
                    break
        
        elif pilih == 2:
            cart()

        elif pilih == 3:
            checkout()
            update()
            while(True):
                money = int(input('Masukkan pembayaran '))
                if money < total:
                    print('Uang kurang')
                elif money > total:
                    print('Uang kembali {}, terima kasih.'.format(money - total))
                    history.clear()
                    break
                elif money == total:
                    print('Uang pas, terima kasih.')
                    history.clear()
                    break

        elif pilih == 4:
            cursor.execute('SELECT namaPembeli, namaPaket, quantity, totalHarga FROM hokben.hokben')
            result = cursor.fetchall()
            df = pd.DataFrame(result)
            print(df)

        elif pilih == 5:
            print('Terima kasih')
            break
        
menu()

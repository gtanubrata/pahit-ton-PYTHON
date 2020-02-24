#Example

# A = [[1, 4, 5, 12], 
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19]]

# print("A =", A) 
# print("A[1] =", A[1])      # 2nd row
# print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

# column = [];        # empty list
# for row in A:
#   column.append(row[2])   

# print("3rd column =", column)


#Rotate clockwise (kanan) test

x = [[1, 2],
     [3, 4]]

x[0][0], x[1][0] = x[1][0], x[0][0]
print(x)

x[0][0], x[0][1] = x[0][1], x[0][0]
print(x)

x[0][1], x[1][1] = x[1][1], x[0][1]
print(x)

# size = 2
# max = 1



y = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y[0][0], y[2][0] = y[2][0], y[0][0]
print(y)

y[0][0], y[0][2] = y[0][2], y[0][0]
print(y)

y[0][2], y[2][2] = y[2][2], y[0][2]
print(y)

y[0][1], y[1][0] = y[1][0], y[0][1]
print(y)

y[0][1], y[1][2] = y[1][2], y[0][1]
print(y)

y[1][2], y[2][1] = y[2][1], y[1][2]
print(y)

# size = 3
# max = 2
# max - 1 = 1

z = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

def print_matrix():
    print(z[0])
    print(z[1])
    print(z[2])
    print(z[3])

def rotate_counterclockwise():
    z[0][0], z[3][0] = z[3][0], z[0][0]
    z[0][0], z[0][3] = z[0][3], z[0][0]
    z[0][3], z[3][3] = z[3][3], z[0][3]
    z[0][1], z[2][0] = z[2][0], z[0][1]
    z[0][1], z[1][3] = z[1][3], z[0][1]
    z[1][3], z[3][2] = z[3][2], z[1][3]
    z[0][2], z[1][0] = z[1][0], z[0][2]
    z[2][3], z[0][2] = z[0][2], z[2][3]
    z[3][1], z[2][3] = z[2][3], z[3][1]
    z[1][1], z[2][1] = z[2][1], z[1][1]
    z[1][1], z[1][2] = z[1][2], z[1][1]
    z[1][2], z[2][2] = z[2][2], z[1][2]

def rotate_clockwise():
    z[0][0], z[0][3] = z[0][3], z[0][0]
    z[0][0], z[3][3] = z[3][3], z[0][0]
    z[0][0], z[3][0] = z[3][0], z[0][0]
    z[0][1], z[1][3] = z[1][3], z[0][1]
    z[0][1], z[2][0] = z[2][0], z[0][1]
    z[2][0], z[3][2] = z[3][2], z[2][0]
    z[2][3], z[0][2] = z[0][2], z[2][3]
    z[0][2], z[1][0] = z[1][0], z[0][2]
    z[1][0], z[3][1] = z[3][1], z[1][0]
    z[1][1], z[1][2] = z[1][2], z[1][1]
    z[1][1], z[2][2] = z[2][2], z[1][1]
    z[1][1], z[2][1] = z[2][1], z[1][1]
    

play = True

while play:

    arah = input("Putar ke mana? (kanan/kiri) ")
    count = int(input("Putar berapa kali? "))
    for i in range(count):
        if arah == "kanan":
            rotate_clockwise()
        else:
            rotate_counterclockwise()
        print_matrix()
        print(f"Putaran ke-{count}")

    play_again = input("Lagi? (y/n): ")
    if play_again == "y":
        z = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    else:
        print("Terima kasih!")
        play = False
# size = 4
# max = 3 = size - 1
# max - 1 = 2
# max - 2 = 1
# etc


z = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

def print_matrix():
    print(z[0])
    print(z[1])
    print(z[2])
    print(z[3])

print_matrix()

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
        print(f"Putaran ke-{i+1}")

    play_again = input("Lagi? (y/n): ")
    if play_again == "y":
        z = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    else:
        print("Terima kasih!")
        play = False



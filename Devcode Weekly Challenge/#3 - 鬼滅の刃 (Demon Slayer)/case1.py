#madebyiffa(077)
#Jumlah Serangan untuk Mengalahkan Iblis
#https://devcode.gethired.id/challenge/share/weekly-challenge-3
#https://devcode.gethired.id/job/share/WFK816

def jumlahSerangan(jumlahIblis):
    #counting how many times a demon can be defeated in one attack
    tanjiro_power = 13
    zenitsu_power = 7
    inosuke_power = 9
    #calculate how many attacks it takes to defeat all the demons
    total_power = tanjiro_power + zenitsu_power + inosuke_power
    serangan_needed = (jumlahIblis + total_power - 1) // total_power
    return serangan_needed

#test cases
print(jumlahSerangan(15))
print(jumlahSerangan(50))
print(jumlahSerangan(200))
print(jumlahSerangan(580))
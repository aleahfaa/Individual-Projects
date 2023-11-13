#madebyiffa(077)
#Jumlah Bayangan yang dibutuhkan Megumi Fushiguro
#https://devcode.gethired.id/challenge/weekly-challenge-1
#https://devcode.gethired.id/job/share/CBG197

def jumlahBayangan(jumlahRohGedungA, jumlahRohGedungB): #number of evil spirits in 2 buildings
    totalRohKutukan = jumlahRohGedungA + jumlahRohGedungB
    return totalRohKutukan * 2

#test case
print(jumlahBayangan(4, 6))
print(jumlahBayangan(3, 5))

#calculate the total of evil spirits in 2 buildings (jumlahRohGedungA+jumlahRohGedungB)
#determine the number of 'bayangan' required to defeat all of the evil spirits
#each 'bayangan' can defeat 1 evil spirit
#total bayangan = totalRohKutukan * 2
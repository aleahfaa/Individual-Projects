#madebyiffa(077)
#Teks Sumpah Pemuda
#https://devcode.gethired.id/challenge/share/weekly-challenge-2
#https://devcode.gethired.id/job/share/IWU488

def teksSumpahPemuda(poin):
    kalimat = ["KAMI PUTRA DAN PUTRI INDONESIA MENGAKU BERTUMPAH DARAH YANG SATU TANAH AIR INDONESIA",
               "KAMI PUTRA DAN PUTRI INDONESIA MENGAKU BERBANGSA YANG SATU BANGSA INDONESIA",
               "KAMI PUTRA DAN PUTRI INDONESIA MENJUNJUNG BAHASA PERSATUAN BAHASA INDONESIA"]
    #if poin in range(1, 4):
    if poin >= 1 and poin <= 3:
        return kalimat[poin - 1]
    else:
        return "KALIMAT TIDAK DITEMUKAN"

#test cases
print(teksSumpahPemuda(1))
print(teksSumpahPemuda(2))
print(teksSumpahPemuda(3))

#create a list 'kalimat' that contains the text of each statement in Sumpah Pemuda
#check if given point is within the range of valid points (1 to 3)
#if it is, return the corresponding statement from 'kalimat'
#if not, return "KALIMAT TIDAK DITEMUKAN"

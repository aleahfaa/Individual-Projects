#madebyiffa(077)
#Daftar Nama Tokoh Penting Sumpah Pemuda
#https://devcode.gethired.id/challenge/share/weekly-challenge-2
#https://devcode.gethired.id/job/share/IWU488

def daftarTokohPenting(daftarNama):
    tokoh_penting = [
        'SOENARIO SASTROWARDOYO',
        'AMIR SYARIFUDDIN HARAHAP',
        'MOHAMMAD YAMIN',
        'DJOKO MARSAID',
        'SOEGONDO DJOJOPOESPITO',
        'JOHANNES LEIMENA',
        'SARMIDI MANGOENSARKORO',
        'JOHAN MOHAMMAD CAI',
        'RUMONDOR CORNELIS LEFRAND SENDUK',
        'MOHAMMAD ROCHJANI SUUD',
        'R KATJA SOENGKANA',
        'WAGE RUDOLF SOEPRATMAN',
        'THEODORA ATHIA SALIM'
    ]

    result = [nama for nama in daftarNama if nama.upper() in tokoh_penting]

    if result:
        return ', '.join(result)
    else:
        return 'NAMA TOKOH PENTING TIDAK DITEMUKAN'

#test cases
print(daftarTokohPenting(["MUHAMMAD JAMALUDIN", "MOHAMMAD YAMIN", "KURLA KURYADI"]))
print(daftarTokohPenting(["JOHAN MOHAMMAD CAI", "SURYANO SANTOSO", "THEODORA ATHIA SALIM", "ATEP SUKENDAR"]))
print(daftarTokohPenting(["MOHAMMAD ROCHJANI SUUD", "RUMONDOR CORNELIS LEFRAND SENDUK", "SARMIDI MANGOENSARKORO", "JOHANNES LEIMENA"]))
print(daftarTokohPenting(["BURYONO KURSUNO", "PURSYANO KARTANO", "BURYO SUKRO", "PAPATARANANG KANARANG"]))

#compares the name in the given list
#return the matching name or message indicating that no figures were found
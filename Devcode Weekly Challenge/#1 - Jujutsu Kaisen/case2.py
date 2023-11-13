#madebyiffa(077)
#Bantu The Angel untuk melepas Segel Prison Realm pada Gojo Satoru
#https://devcode.gethired.id/challenge/weekly-challenge-1
#https://devcode.gethired.id/job/share/CBG197

def memecahkanKode(kode):
    hasil = []
    for karakter in kode:
        if karakter.isdigit():
            hasil.append(karakter)
    return ''.join(hasil)

#test case
print(memecahkanKode('KD89L3K1A2BD'))
print(memecahkanKode('H21P45A8XSP'))

#iterate every karakter in the given kode and check if it's a digit
#if it is, the function will append it to a list
#the function will convert the list of digits into a string and return it
#assume that the given kode will always contain at least one digit
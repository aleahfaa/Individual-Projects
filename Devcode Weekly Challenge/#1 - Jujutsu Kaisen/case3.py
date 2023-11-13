#madebyiffa(077)
#Pemenang Pertarungan Yuji Itadori melawan Roh Kutukan
#https://devcode.gethired.id/challenge/weekly-challenge-1
#https://devcode.gethired.id/job/share/CBG197

def pemenangPertarungan(yujiltadori, rohKutukan):
    unggulan_yuji = sum(1 for i in range(len(yujiltadori)) if yujiltadori[i] > rohKutukan[i])
    unggulan_roh = sum(1 for i in range(len(rohKutukan)) if rohKutukan[i] > yujiltadori[i])

    if unggulan_yuji > unggulan_roh:
        return 'Yuji Itadori'
    elif unggulan_roh > unggulan_yuji:
        return 'Roh Kutukan'
    else:
        return 'Keduanya Imbang'

#test case
print(pemenangPertarungan([100,80,90], [90,100,70]))
print(pemenangPertarungan([80,80,90], [100,90,90]))
print(pemenangPertarungan([70,80,90], [90,70,90]))

#we compare each element of the arrays 'yujiltadori' and 'rohKutukan'
#count the number of times an element in 'yujiltadori' and 'rohKutukan'
#if 'yujiltadori' > 'rohKutukan', store the count in 'unggulan_yuji', return 'Yuji Itadori'
#if 'yujiltadori' < 'rohKutukan', store the count in 'unggulan_roh', return 'Roh Kutukan'
#if 'yujiltadori' = 'rohKutukan', return 'Keduanya Imbang'
